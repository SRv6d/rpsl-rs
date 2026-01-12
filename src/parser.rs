use std::fmt;
use winnow::{
    ascii::{multispace0, newline, space0},
    combinator::{alt, cut_err, delimited, peek, preceded, repeat, terminated},
    error::{ContextError, ErrMode, StrContext, StrContextValue},
    token::{one_of, take_till, take_while},
    Parser,
};

use crate::{Attribute, Name, Object, Value};

/// Parse RPSL into an [`Object`], borrowing from the source.
///
/// ```text
/// role:           ACME Company
/// address:        Packet Street 6
/// address:        128 Series of Tubes
/// address:        Internet
/// email:          rpsl-rs@github.com
/// nic-hdl:        RPSL1-RIPE
/// source:         RIPE
///                        ↓
/// role:           ACME Company ◀─────────────── &"role":      &"ACME Company"
/// address:        Packet Street 6 ◀──────────── &"address":   &"Packet Street 6"
/// address:        128 Series of Tubes ◀──────── &"address":   &"128 Series of Tubes"
/// address:        Internet ◀─────────────────── &"address":   &"Internet"
/// email:          rpsl-rs@github.com ◀───────── &"email":     &"rpsl-rs@github.com"
/// nic-hdl:        RPSL1-RIPE ◀───────────────── &"nic-hdl":   &"RPSL1-RIPE"
/// source:         RIPE ◀─────────────────────── &"source":    &"RIPE"
/// ```
///
/// # Errors
/// Returns a [`ParseError`] if the input cannot be parsed into an object. Parsing is lenient
/// and does not validate attribute names or values; use [`Object::validate`] or
/// [`Object::into_spec`] to enforce a specification after parsing.
///
/// # Examples
/// ```
/// # use rpsl::{parse_object, object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let role_acme = "
/// role:        ACME Company
/// address:     Packet Street 6
/// address:     128 Series of Tubes
/// address:     Internet
/// email:       rpsl-rs@github.com
/// nic-hdl:     RPSL1-RIPE
/// source:      RIPE
///
/// ";
/// let parsed = parse_object(role_acme)?;
/// assert_eq!(
///     parsed,
///     object! {
///         "role": "ACME Company";
///         "address": "Packet Street 6";
///         "address": "128 Series of Tubes";
///         "address": "Internet";
///         "email": "rpsl-rs@github.com";
///         "nic-hdl": "RPSL1-RIPE";
///         "source": "RIPE";
///     }
/// );
/// # Ok(())
/// # }
/// ```
///
/// Values spread over multiple lines can be parsed too.
/// ```
/// # use rpsl::{parse_object, object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let multiline_remark = "
/// remarks:     Value 1
///              Value 2
///
/// ";
/// assert_eq!(
///     parse_object(multiline_remark)?,
///     object! {
///         "remarks": "Value 1", "Value 2";
///     }
/// );
/// # Ok(())
/// # }
/// ```
///
/// An attribute that does not have a value is valid.
/// ```
/// # use rpsl::{parse_object, object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let without_value = "
/// as-name:     REMARKABLE
/// remarks:
/// remarks:     ^^^^^^^^^^ nothing here
///
/// ";
/// assert_eq!(
///     parse_object(without_value)?,
///     object! {
///         "as-name": "REMARKABLE";
///         "remarks": "";
///         "remarks": "^^^^^^^^^^ nothing here";
///     }
/// );
/// # Ok(())
/// # }
/// ```
///
/// The same goes for values containing only whitespace.
/// Since whitespace to the left of a value is trimmed, they are equivalent to no value.
///
/// ```
/// # use rpsl::{parse_object, object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let whitespace_value = "
/// as-name:     REMARKABLE
/// remarks:               
/// remarks:     ^^^^^^^^^^ nothing but hot air (whitespace)
///
/// ";
/// assert_eq!(
///     parse_object(whitespace_value)?,
///     object! {
///         "as-name": "REMARKABLE";
///         "remarks": "";
///         "remarks": "^^^^^^^^^^ nothing but hot air (whitespace)";
///     }
/// );
/// # Ok(())
/// # }
/// ```
pub fn parse_object(rpsl: &str) -> Result<Object<'_>, ParseError> {
    let o = object_block().parse(rpsl)?;
    Ok(o)
}

/// Parse a WHOIS server response into [`Object`]s contained within.
///
/// # Errors
/// Returns a [`ParseError`] if the input cannot be parsed into objects. Parsing is lenient and
/// does not validate attribute names or values; use [`Object::validate`] or [`Object::into_spec`]
/// to enforce a specification after parsing.
///
/// # Examples
/// ```
/// # use rpsl::{parse_whois_response, object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let whois_response = "
/// ASNumber:       32934
/// ASName:         FACEBOOK
/// ASHandle:       AS32934
/// RegDate:        2004-08-24
/// Updated:        2012-02-24
/// Comment:        Please send abuse reports to abuse@facebook.com
/// Ref:            https://rdap.arin.net/registry/autnum/32934
///
///
/// OrgName:        Facebook, Inc.
/// OrgId:          THEFA-3
/// Address:        1601 Willow Rd.
/// City:           Menlo Park
/// StateProv:      CA
/// PostalCode:     94025
/// Country:        US
/// RegDate:        2004-08-11
/// Updated:        2012-04-17
/// Ref:            https://rdap.arin.net/registry/entity/THEFA-3
///
/// ";
/// let objects = parse_whois_response(whois_response)?;
/// assert_eq!(
///     objects,
///     vec![
///             object! {
///                 "ASNumber": "32934";
///                 "ASName": "FACEBOOK";
///                 "ASHandle": "AS32934";
///                 "RegDate": "2004-08-24";
///                 "Updated": "2012-02-24";
///                 "Comment": "Please send abuse reports to abuse@facebook.com";
///                 "Ref": "https://rdap.arin.net/registry/autnum/32934";
///             },
///             object! {
///                 "OrgName": "Facebook, Inc.";
///                 "OrgId": "THEFA-3";
///                 "Address": "1601 Willow Rd.";
///                 "City": "Menlo Park";
///                 "StateProv": "CA";
///                 "PostalCode": "94025";
///                 "Country": "US";
///                 "RegDate": "2004-08-11";
///                 "Updated": "2012-04-17";
///                 "Ref": "https://rdap.arin.net/registry/entity/THEFA-3";
///             }
///         ]
/// );
/// # Ok(())
/// # }
pub fn parse_whois_response(response: &str) -> Result<Vec<Object<'_>>, ParseError> {
    let block_parser = object_block_padded(object_block());
    let objects = repeat(1.., block_parser).parse(response)?;
    Ok(objects)
}

/// Parse a list of attributes that make up an object.
///
/// Consumes optional surrounding whitespace, then reads attributes
/// until the mandatory blank line that terminates the object.
fn object_block<'s>() -> impl Parser<&'s str, Object<'s>, ErrMode<ContextError>> {
    // a list of attributes that ends when a blank line is encountered, as per RFC 2622.
    let object = terminated(repeat(1.., attribute()), newline);

    // allow for some optional padding
    delimited(multispace0, object, multispace0)
        .with_taken()
        .map(|(attributes, source)| Object::new_parsed(source, attributes))
}

/// Generate a parser that extends the given object block parser to consume optional padding
/// server messages or newlines.
fn object_block_padded<'s, P>(
    block_parser: P,
) -> impl Parser<&'s str, Object<'s>, ErrMode<ContextError>>
where
    P: Parser<&'s str, Object<'s>, ErrMode<ContextError>>,
{
    delimited(
        consume_opt_messages_or_newlines(),
        block_parser,
        consume_opt_messages_or_newlines(),
    )
}

/// Consume optional messages or newlines.
fn consume_opt_messages_or_newlines<'s>() -> impl Parser<&'s str, (), ErrMode<ContextError>> {
    repeat(0.., alt((newline.void(), server_message().void())))
}

// A response code or message sent by the whois server.
// Starts with the "%" character and extends until the end of the line.
fn server_message<'s>() -> impl Parser<&'s str, &'s str, ErrMode<ContextError>> {
    delimited(
        ('%', space0),
        take_while(0.., |c: char| !c.is_control()),
        newline,
    )
}

/// Parse an attribute value pair.
fn attribute<'s>() -> impl Parser<&'s str, Attribute<'s>, ErrMode<ContextError>> {
    move |input: &mut &'s str| {
        let name: Name<'s> = take_till(1.., |c| c == ':' || c == ';' || c == '\n')
            .map(Name::from_parsed)
            .context(StrContext::Label("attribute name"))
            .parse_next(input)?;

        // consume the separator
        cut_err(
            ':'.context(StrContext::Label("separator"))
                .context(StrContext::Expected(StrContextValue::StringLiteral(":"))),
        )
        .parse_next(input)?;
        // and optionally any following spaces
        space0.parse_next(input)?;

        let value = attribute_value().parse_next(input)?;

        Ok(Attribute::new(name, value))
    }
}

/// Parse an attribute value with optional continuation lines.
fn attribute_value<'s>() -> impl Parser<&'s str, Value<'s>, ErrMode<ContextError>> {
    move |input: &mut &'s str| {
        let value = || terminated(take_till(0.., |c| c == '\n'), newline);

        let first = value().parse_next(input)?;

        if peek(continuation_char()).parse_next(input).is_ok() {
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

/// Parse a single continuation character.
fn continuation_char<'s>() -> impl Parser<&'s str, char, ErrMode<ContextError>> {
    one_of([' ', '\t', '+'])
}

/// An error that can occur when parsing RPSL text.
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

        let mut parser = object_block();
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

        let mut parser = object_block();
        let parsed = parser.parse_next(rpsl).unwrap();

        assert_eq!(parsed.source().unwrap(), source);
    }

    #[test]
    fn object_block_without_newline_termination_is_err() {
        let object = &mut concat!(
            "email:       rpsl-rs@github.com\n",
            "nic-hdl:     RPSL1-RIPE\n",
        );
        let mut parser = object_block();
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

        let mut parser = object_block_padded(object_block());
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
        let mut parser = consume_opt_messages_or_newlines();
        parser.parse_next(given).unwrap();
        assert_eq!(*given, "");
    }

    #[test]
    fn optional_comment_or_newlines_optional() {
        let mut parser = consume_opt_messages_or_newlines();
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
        let mut parser = server_message();
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
        let mut parser = attribute();
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
        let mut parser = attribute();
        let parsed = parser.parse_next(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    #[rstest]
    #[case(
        &mut "OrgName;        Facebook, Inc.\n",
        "\
parse error at line 1, column 8
  |
1 | OrgName;        Facebook, Inc.
  |        ^
invalid separator
expected `:`"
    )]
    fn attribute_invalid_separator_is_expected_err_msg(
        #[case] given: &mut &str,
        #[case] expected_msg: &str,
    ) {
        let mut parser = attribute();
        let err = parser.parse(given).unwrap_err();
        assert_eq!(err.to_string(), expected_msg);
    }
}
