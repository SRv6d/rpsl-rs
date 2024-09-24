use std::iter::once;

use winnow::{
    ascii::{newline, space0},
    combinator::{delimited, opt, preceded, repeat, separated_pair, terminated},
    error::ParserError,
    token::{one_of, take_while},
    Parser,
};

use crate::{Attribute, Name, Value};

// A response code or message sent by the whois server.
// Starts with the "%" character and extends until the end of the line.
// In contrast to RPSL, characters are not limited to ASCII.
pub fn server_message<'s, E>() -> impl Parser<&'s str, &'s str, E>
where
    E: ParserError<&'s str>,
{
    delimited(
        ('%', space0),
        take_while(0.., |c: char| !c.is_control()),
        newline,
    )
}

// Generate an attribute parser.
// The attributes name and value are separated by a colon and optional spaces.
pub fn attribute<'s, E>() -> impl Parser<&'s str, Attribute<'s>, E>
where
    E: ParserError<&'s str>,
{
    separated_pair(attribute_name(), (':', space0), attribute_value_opt_multi())
        .map(|(name, value)| Attribute::new(name, value))
}

/// Generate an attribute value parser that parses an ASCII sequence of letters,
/// digits and the characters "-", "_". The first character must be a letter,
/// while the last character may be a letter or a digit.
fn attribute_name<'s, E>() -> impl Parser<&'s str, Name<'s>, E>
where
    E: ParserError<&'s str>,
{
    take_while(2.., ('A'..='Z', 'a'..='z', '0'..='9', '-', '_'))
        .verify(|s: &str| {
            s.starts_with(|c: char| c.is_ascii_alphabetic())
                && s.ends_with(|c: char| c.is_ascii_alphanumeric())
        })
        .map(Name::unchecked)
}

/// Generate an attribute value parser.
fn attribute_value<'s, E>() -> impl Parser<&'s str, &'s str, E>
where
    E: ParserError<&'s str>,
{
    terminated(
        take_while(0.., |c| Value::validate_char(c).is_ok()),
        newline,
    )
}

/// Generate a parser for continuation values.
fn attribute_value_continuation<'s, P, E>(value_parser: P) -> impl Parser<&'s str, Vec<&'s str>, E>
where
    P: Parser<&'s str, &'s str, E>,
    E: ParserError<&'s str>,
{
    repeat(
        1..,
        preceded(continuation_char(), preceded(space0, value_parser)),
    )
}

/// Generate an attribute value parser that optionally parses continuation lines.
fn attribute_value_opt_multi<'s, E>() -> impl Parser<&'s str, Value<'s>, E>
where
    E: ParserError<&'s str>,
{
    (
        attribute_value(),
        opt(attribute_value_continuation(attribute_value())),
    )
        .map(|(first_value, continuation)| {
            if let Some(continuation_values) = continuation {
                Value::unchecked_multi(once(first_value).chain(continuation_values))
            } else {
                Value::unchecked_single(first_value)
            }
        })
}

/// Generate a parser for a single continuation character.
fn continuation_char<'s, E>() -> impl Parser<&'s str, char, E>
where
    E: ParserError<&'s str>,
{
    one_of([' ', '\t', '+'])
}

#[cfg(test)]
mod tests {
    use proptest::prelude::*;
    use rstest::*;
    use winnow::error::ContextError;

    use super::*;

    #[rstest]
    #[case(
        &mut "% Note: this output has been filtered.\n",
        "Note: this output has been filtered.",
        ""
    )]
    #[case(
        &mut "%       To receive output for a database update, use the \"-B\" flag.\n",
        "To receive output for a database update, use the \"-B\" flag.",
        ""
    )]
    #[case(
        &mut "% This query was served by the RIPE Database Query Service version 1.106.1 (BUSA)\n",
        "This query was served by the RIPE Database Query Service version 1.106.1 (BUSA)",
        ""
    )]
    fn server_message_valid(
        #[case] given: &mut &str,
        #[case] expected: &str,
        #[case] remaining: &str,
    ) {
        let mut parser = server_message::<ContextError>();
        let parsed = parser.parse_next(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    #[rstest]
    #[case(
        &mut "import:         from AS12 accept AS12\n",
        Attribute::unchecked_single("import", "from AS12 accept AS12"),
        ""
    )]
    fn attribute_valid_single_value(
        #[case] given: &mut &str,
        #[case] expected: Attribute,
        #[case] remaining: &str,
    ) {
        let parsed = attribute::<ContextError>().parse_next(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    #[rstest]
    #[case(
        &mut concat!(
            "remarks:        Locations\n",
            "                LA1 - CoreSite One Wilshire\n",
            "                NY1 - Equinix New York, Newark\n",
            "remarks:        Peering Policy\n",
        ),
        Attribute::unchecked_multi(
            "remarks",
            vec![
                "Locations",
                "LA1 - CoreSite One Wilshire",
                "NY1 - Equinix New York, Newark",
            ]
        ),
        "remarks:        Peering Policy\n"
    )]
    fn attribute_valid_multi_value(
        #[case] given: &mut &str,
        #[case] expected: Attribute,
        #[case] remaining: &str,
    ) {
        let parsed = attribute::<ContextError>().parse_next(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    #[rstest]
    #[case(&mut "remarks:", "remarks", ":")]
    #[case(&mut "aut-num:", "aut-num", ":")]
    #[case(&mut "ASNumber:", "ASNumber", ":")]
    #[case(&mut "route6:", "route6", ":")]
    fn attribute_name_valid(
        #[case] given: &mut &str,
        #[case] expected: &str,
        #[case] remaining: &str,
    ) {
        let mut parser = attribute_name::<ContextError>();
        let parsed = parser.parse_next(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    #[rstest]
    #[case(&mut "1remarks:")]
    #[case(&mut "-remarks:")]
    #[case(&mut "_remarks:")]
    fn attribute_name_non_letter_first_char_is_error(#[case] given: &mut &str) {
        let mut parser = attribute_name::<ContextError>();
        assert!(parser.parse_next(given).is_err());
    }

    #[rstest]
    #[case(&mut "remarks-:")]
    #[case(&mut "remarks_:")]
    fn attribute_name_non_letter_or_digit_last_char_is_error(#[case] given: &mut &str) {
        let mut parser = attribute_name::<ContextError>();
        assert!(parser.parse_next(given).is_err());
    }

    #[test]
    fn attribute_name_single_letter_is_error() {
        let mut parser = attribute_name::<ContextError>();
        assert!(parser.parse_next(&mut "a").is_err());
    }

    #[rstest]
    #[case(
            &mut "This is an example remark\n",
            "This is an example remark",
            ""
        )]
    #[case(
            &mut "Concerning abuse and spam ... mailto: abuse@asn.net\n",
            "Concerning abuse and spam ... mailto: abuse@asn.net",
            ""
        )]
    #[case(
            &mut "+49 176 07071964\n",
            "+49 176 07071964",
            ""
        )]
    #[case(
            &mut "* Equinix FR5, Kleyerstr, Frankfurt am Main\n",
            "* Equinix FR5, Kleyerstr, Frankfurt am Main",
            ""
        )]
    fn attribute_value_valid(
        #[case] given: &mut &str,
        #[case] expected: &str,
        #[case] remaining: &str,
    ) {
        let mut parser = attribute_value::<ContextError>();
        let parsed = parser.parse_next(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    proptest! {
        /// Parsing any non extended ASCII returns an error.
        #[test]
        fn attribute_value_non_extended_ascii_is_err(s in r"[^\x00-\xFF]+") {
            let mut parser = attribute_value::<ContextError>();
            assert!(parser.parse_next(&mut s.as_str()).is_err());
        }
    }

    #[rstest]
    #[case(
            &mut "    continuation value prefixed by a space\n",
            vec!["continuation value prefixed by a space"],
            ""
        )]
    #[case(
            &mut "\t    continuation value prefixed by a tab\n",
            vec!["continuation value prefixed by a tab"],
            ""
        )]
    #[case(
            &mut "+    continuation value prefixed by a plus\n",
            vec!["continuation value prefixed by a plus"],
            ""
        )]
    fn attribute_value_continuation_valid(
        #[case] given: &mut &str,
        #[case] expected: Vec<&str>,
        #[case] remaining: &str,
    ) {
        let value_parser = attribute_value::<ContextError>();
        let mut continuation_parser = attribute_value_continuation::<_, ContextError>(value_parser);
        let parsed = continuation_parser.parse_next(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }
}
