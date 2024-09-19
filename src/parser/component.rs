use std::iter::once;

use winnow::{
    ascii::{newline, space0},
    combinator::{delimited, peek, preceded, repeat, separated_pair, terminated},
    error::ParserError,
    stream::{ContainsToken, Stream, StreamIsPartial},
    token::{one_of, take_while},
    PResult, Parser,
};

use super::spec::ValueSpec;
use crate::Attribute;

// A response code or message sent by the whois server.
// Starts with the "%" character and extends until the end of the line.
// In contrast to RPSL, characters are not limited to ASCII.
pub fn server_message<'s>(input: &mut &'s str) -> PResult<&'s str> {
    delimited(
        ('%', space0),
        take_while(0.., |c: char| !c.is_control()),
        newline,
    )
    .parse_next(input)
}

// A RPSL attribute consisting of a name and one or more values.
// The name is followed by a colon and optional spaces.
// Single value attributes are limited to one line, while multi value attributes span over multiple lines.
pub fn attribute<'s>(input: &mut &'s str) -> PResult<Attribute<'s>> {
    let (name, first_value) = separated_pair(
        terminated(attribute_name, ':'),
        space0,
        terminated(attribute_value(ValueSpec::default()), newline),
    )
    .parse_next(input)?;

    if peek(consume_continuation_char).parse_next(input).is_ok() {
        let continuation_values: Vec<&str> = repeat(1.., continuation_line).parse_next(input)?;
        return Ok(Attribute::unchecked_multi(
            name,
            once(first_value).chain(continuation_values),
        ));
    }

    Ok(Attribute::unchecked_single(name, first_value))
}

// An ASCII sequence of letters, digits and the characters "-", "_".
// The first character must be a letter, while the last character may be a letter or a digit.
fn attribute_name<'s>(input: &mut &'s str) -> PResult<&'s str> {
    take_while(2.., ('A'..='Z', 'a'..='z', '0'..='9', '-', '_'))
        .verify(|s: &str| {
            s.starts_with(|c: char| c.is_ascii_alphabetic())
                && s.ends_with(|c: char| c.is_ascii_alphanumeric())
        })
        .parse_next(input)
}

/// Generate an attribute value parser from a set of valid tokens.
fn attribute_value<S, I, E>(set: S) -> impl Parser<I, <I as Stream>::Slice, E>
where
    S: ContainsToken<<I as Stream>::Token>,
    I: StreamIsPartial + Stream,
    E: ParserError<I>,
{
    take_while(0.., set)
}

// Extends an attributes value over multiple lines.
// Must start with a space, tab or a plus character.
pub fn continuation_line<'s>(input: &mut &'s str) -> PResult<&'s str> {
    delimited(
        consume_continuation_char,
        preceded(space0, attribute_value(ValueSpec::default())),
        newline,
    )
    .parse_next(input)
}

// Consume a single multiline continuation character.
pub fn consume_continuation_char(input: &mut &str) -> PResult<()> {
    one_of([' ', '\t', '+']).void().parse_next(input)
}
#[cfg(test)]
mod tests {
    use rstest::*;

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
        let parsed = server_message(given).unwrap();
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
        let parsed = attribute(given).unwrap();
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
        let parsed = attribute(given).unwrap();
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
        let parsed = attribute_name(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    #[rstest]
    #[case(&mut "1remarks:")]
    #[case(&mut "-remarks:")]
    #[case(&mut "_remarks:")]
    fn attribute_name_non_letter_first_char_is_error(#[case] given: &mut &str) {
        assert!(attribute_name(given).is_err());
    }

    #[rstest]
    #[case(&mut "remarks-:")]
    #[case(&mut "remarks_:")]
    fn attribute_name_non_letter_or_digit_last_char_is_error(#[case] given: &mut &str) {
        assert!(attribute_name(given).is_err());
    }

    #[test]
    fn attribute_name_single_letter_is_error() {
        assert!(attribute_name(&mut "a").is_err());
    }

    #[rstest]
    #[case(
        ValueSpec::Rfc2622,
        &mut "This is an example remark\n",
        "This is an example remark",
        "\n"
    )]
    #[case(
        ValueSpec::Rfc2622,
        &mut "Concerning abuse and spam ... mailto: abuse@asn.net\n",
        "Concerning abuse and spam ... mailto: abuse@asn.net",
        "\n"
    )]
    #[case(
        ValueSpec::Rfc2622,
        &mut "+49 176 07071964\n",
        "+49 176 07071964",
        "\n"
    )]
    #[case(
        ValueSpec::Rfc2622,
        &mut "* Equinix FR5, Kleyerstr, Frankfurt am Main\n",
        "* Equinix FR5, Kleyerstr, Frankfurt am Main",
        "\n"
    )]
    #[case(
        ValueSpec::Rfc2622,
        &mut "\n",
        "",
        "\n"
    )]
    fn attribute_value_valid(
        #[case] spec: ValueSpec,
        #[case] given: &mut &str,
        #[case] expected: &str,
        #[case] remaining: &str,
    ) {
        use winnow::error::ContextError;

        let mut parser = attribute_value::<_, &str, ContextError<&str>>(spec);
        let parsed = parser.parse_next(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    #[rstest]
    #[case(
        &mut "    continuation value prefixed by a space\n",
        "continuation value prefixed by a space",
        ""
    )]
    #[case(
        &mut "\t    continuation value prefixed by a tab\n",
        "continuation value prefixed by a tab",
        ""
    )]
    #[case(
        &mut "+    continuation value prefixed by a plus\n",
        "continuation value prefixed by a plus",
        ""
    )]
    fn continuation_line_valid(
        #[case] given: &mut &str,
        #[case] expected: &str,
        #[case] remaining: &str,
    ) {
        let parsed = continuation_line(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }
}
