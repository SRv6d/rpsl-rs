use winnow::{
    ascii::{newline, space0},
    combinator::{alt, delimited, peek, preceded, repeat, separated_pair, terminated},
    error::{AddContext, ContextError, ParserError, StrContext, StrContextValue},
    token::{one_of, take_while},
    Parser,
};

use crate::{Attribute, Name, Object, Value};

/// Generate an object block parser.
/// As per [RFC 2622](https://datatracker.ietf.org/doc/html/rfc2622#section-2), an RPSL object
/// is textually represented as a list of attribute-value pairs that ends when a blank line is encountered.
pub fn object_block<'s, E>() -> impl Parser<&'s str, Object<'s>, E>
where
    E: ParserError<&'s str> + AddContext<&'s str, StrContext>,
{
    terminated(repeat(1.., attribute()), newline)
        .with_taken()
        .map(|(attributes, source)| Object::from_parsed(source, attributes))
}

/// Generate a parser that extends the given object block parser to consume optional padding
/// server messages or newlines.
pub fn object_block_padded<'s, P, E>(block_parser: P) -> impl Parser<&'s str, Object<'s>, E>
where
    P: Parser<&'s str, Object<'s>, E>,
    E: ParserError<&'s str>,
{
    delimited(
        consume_opt_messages_or_newlines(),
        block_parser,
        consume_opt_messages_or_newlines(),
    )
}

/// Generate a parser that consumes optional messages or newlines.
fn consume_opt_messages_or_newlines<'s, E>() -> impl Parser<&'s str, (), E>
where
    E: ParserError<&'s str>,
{
    repeat(0.., alt((newline.void(), server_message().void())))
}

// A response code or message sent by the whois server.
// Starts with the "%" character and extends until the end of the line.
// In contrast to RPSL, characters are not limited to ASCII.
fn server_message<'s, E>() -> impl Parser<&'s str, &'s str, E>
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
fn attribute<'s, E>() -> impl Parser<&'s str, Attribute<'s>, E>
where
    E: ParserError<&'s str> + AddContext<&'s str, StrContext>,
{
    separated_pair(
        attribute_name(),
        (
            ':'.context(StrContext::Label("separator"))
                .context(StrContext::Expected(StrContextValue::StringLiteral(":"))),
            space0,
        ),
        attribute_value(),
    )
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

/// Generate an attribute value parser that includes continuation lines.
fn attribute_value<'s, E>() -> impl Parser<&'s str, Value<'s>, E>
where
    E: ParserError<&'s str>,
{
    move |input: &mut &'s str| {
        let first_value = single_attribute_value().parse_next(input)?;

        if peek(continuation_char::<ContextError>())
            .parse_next(input)
            .is_ok()
        {
            let mut continuation_values: Vec<&str> = repeat(
                1..,
                preceded(
                    continuation_char(),
                    preceded(space0, single_attribute_value()),
                ),
            )
            .parse_next(input)?;
            continuation_values.insert(0, first_value);
            return Ok(Value::unchecked_multi(continuation_values));
        }

        Ok(Value::unchecked_single(first_value))
    }
}

/// Generate a parser for a singular attribute value without continuation.
fn single_attribute_value<'s, E>() -> impl Parser<&'s str, &'s str, E>
where
    E: ParserError<&'s str>,
{
    terminated(
        take_while(0.., |c| Value::validate_char(c).is_ok()),
        newline,
    )
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
        &mut concat!(
            "email:       rpsl-rs@github.com\n",
            "nic-hdl:     RPSL1-RIPE\n",
            "\n"
        ),
        vec![
                Attribute::unchecked_single("email", "rpsl-rs@github.com"),
                Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE")
        ]
    )]
    fn object_block_valid(#[case] given: &mut &str, #[case] attributes: Vec<Attribute>) {
        let expected = Object::from_parsed(given, attributes);

        let mut parser = object_block::<ContextError>();
        let parsed = parser.parse_next(given).unwrap();

        assert_eq!(parsed, expected);
    }

    #[test]
    /// When parsing RPSL, the resulting object contains the original source it was created from.
    fn object_block_parsed_object_contains_source() {
        let rpsl = &mut concat!(
            "email:       rpsl-rs@github.com\n",
            "nic-hdl:     RPSL1-RIPE\n",
            "\n"
        );
        let source = *rpsl;

        let mut parser = object_block::<ContextError>();
        let parsed = parser.parse_next(rpsl).unwrap();

        assert_eq!(parsed.source().unwrap(), source);
    }

    #[test]
    fn object_block_without_newline_termination_is_err() {
        let object = &mut concat!(
            "email:       rpsl-rs@github.com\n",
            "nic-hdl:     RPSL1-RIPE\n",
        );
        let mut parser = object_block::<ContextError>();
        assert!(parser.parse_next(object).is_err());
    }

    #[rstest]
    #[case(
        &mut concat!(
            "\n\n",
            "email:       rpsl-rs@github.com\n",
            "nic-hdl:     RPSL1-RIPE\n",
            "\n",
            "\n\n\n"
        ),
        vec![
                Attribute::unchecked_single("email", "rpsl-rs@github.com"),
                Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE")
        ]
    )]
    fn object_block_padded_valid(#[case] given: &mut &str, #[case] attributes: Vec<Attribute>) {
        let expected = Object::from_parsed(given, attributes);

        let mut parser = object_block_padded::<_, ContextError>(object_block());
        let parsed = parser.parse_next(given).unwrap();

        assert_eq!(parsed, expected);
    }

    #[rstest]
    #[case(
        &mut "% Note: This is a server message\n"
    )]
    #[case(
        &mut concat!(
            "\n",
            "% Note: This is a server message followed by an empty line\n"
        )
    )]
    #[case(
        &mut concat!(
            "% Note: This is a server message preceding some newlines.\n",
            "\n",
            "\n",
        )
    )]
    fn optional_comment_or_newlines_consumed(#[case] given: &mut &str) {
        let mut parser = consume_opt_messages_or_newlines::<ContextError>();
        parser.parse_next(given).unwrap();
        assert_eq!(*given, "");
    }

    #[test]
    fn optional_comment_or_newlines_optional() {
        let mut parser = consume_opt_messages_or_newlines::<ContextError>();
        assert_eq!(parser.parse_next(&mut ""), Ok(()));
    }

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
        let mut parser = attribute::<ContextError>();
        let parsed = parser.parse_next(given).unwrap();
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
    #[case(
        &mut concat!(
            "remarks:        Test\n",
            "                continuation value prefixed by a space\n",
            "\t              continuation value prefixed by a tab\n",
            "+               continuation value prefixed by a plus\n",
        ),
        Attribute::unchecked_multi(
            "remarks",
            vec![
                "Test",
                "continuation value prefixed by a space",
                "continuation value prefixed by a tab",
                "continuation value prefixed by a plus"
            ]
        ),
        ""
    )]
    fn attribute_valid_multi_value(
        #[case] given: &mut &str,
        #[case] expected: Attribute,
        #[case] remaining: &str,
    ) {
        let mut parser = attribute::<ContextError>();
        let parsed = parser.parse_next(given).unwrap();
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
        let mut parser = single_attribute_value::<ContextError>();
        let parsed = parser.parse_next(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    proptest! {
        /// Parsing any non extended ASCII returns an error.
        #[test]
        fn attribute_value_non_extended_ascii_is_err(s in r"[^\x00-\xFF]+") {
            let mut parser = single_attribute_value::<ContextError>();
            assert!(parser.parse_next(&mut s.as_str()).is_err());
        }
    }
}
