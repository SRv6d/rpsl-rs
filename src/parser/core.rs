use std::fmt;
use winnow::{
    ascii::{newline, space0},
    combinator::{alt, delimited, peek, preceded, repeat, terminated},
    error::{AddContext, ContextError, ParserError, StrContext, StrContextValue},
    token::{one_of, take_till, take_while},
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
        .map(|(attributes, source)| Object::new_parsed(source, attributes))
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
    move |input: &mut &'s str| {
        let name: Name<'s> = take_till(1.., |c| c == ':')
            .map(Name::from_parsed)
            .context(StrContext::Label("attribute name"))
            .parse_next(input)?;

        // consume the separator and optionally any following spaces
        ':'.context(StrContext::Label("separator"))
            .context(StrContext::Expected(StrContextValue::StringLiteral(":")))
            .parse_next(input)?;
        space0.parse_next(input)?;

        let value = attribute_value().parse_next(input)?;

        Ok(Attribute::new(name, value))
    }
}

/// Generate an attribute value parser that includes continuation lines.
fn attribute_value<'s, E>() -> impl Parser<&'s str, Value<'s>, E>
where
    E: ParserError<&'s str>,
{
    move |input: &mut &'s str| {
        let value = || terminated(take_till(0.., |c| c == '\n'), newline);

        let first = value().parse_next(input)?;

        if peek(continuation_char::<ContextError>())
            .parse_next(input)
            .is_ok()
        {
            let mut continuation: Vec<&str> = repeat(
                1..,
                preceded(continuation_char(), preceded(space0, value())),
            )
            .parse_next(input)?;
            continuation.insert(0, first);
            Ok(Value::from_parsed_multi(continuation))
        } else {
            Ok(Value::from_parsed_single(first))
        }
    }
}

/// Generate a parser for a single continuation character.
fn continuation_char<'s, E>() -> impl Parser<&'s str, char, E>
where
    E: ParserError<&'s str>,
{
    one_of([' ', '\t', '+'])
}

/// An error that can occur when parsing RPSL text.
///
/// # Example
/// ```
/// # use rpsl::parse_object;
/// let rpsl = "\
/// role;        ACME Company
///
/// ";
/// let err = parse_object(rpsl).unwrap_err();
/// let message = "\
/// parse error at line 1, column 5
///   |
/// 1 | role;        ACME Company
///   |     ^
/// invalid separator
/// expected `:`";
/// assert_eq!(err.to_string(), message);
/// ```
#[derive(thiserror::Error, Debug)]
pub struct ParseError(String);

impl fmt::Display for ParseError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.0)
    }
}

impl From<winnow::error::ParseError<&str, winnow::error::ContextError>> for ParseError {
    fn from(value: winnow::error::ParseError<&str, winnow::error::ContextError>) -> Self {
        Self(value.to_string())
    }
}

#[cfg(test)]
mod tests {
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
        let expected = Object::new_parsed(given, attributes);

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
        let expected = Object::new_parsed(given, attributes);

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
}
