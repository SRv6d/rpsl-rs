use super::component;
use crate::rpsl::Object;
use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::{multispace0, newline},
    combinator::all_consuming,
    error::Error,
    multi::{many0, many1},
    sequence::{delimited, terminated},
    Finish, IResult,
};

/// Parse an object with at least one attribute terminated by a newline.
///
/// As per [RFC 2622](https://datatracker.ietf.org/doc/html/rfc2622#section-2), an RPSL object
/// is textually represented as a list of attribute-value pairs that ends when a blank line is encountered.
fn object_block(input: &str) -> IResult<&str, Object> {
    let (remaining, attributes) = terminated(many1(component::attribute), newline)(input)?;
    Ok((remaining, attributes.into()))
}

/// Uses the object block parser but allows for optinal padding with server messages or newlines.
fn padded_object_block(input: &str) -> IResult<&str, Object> {
    let (remaining, object) = delimited(
        optional_message_or_newlines,
        object_block,
        optional_message_or_newlines,
    )(input)?;
    Ok((remaining, object))
}

/// Parse an unlimited number of optional server messages or newlines.
fn optional_message_or_newlines(input: &str) -> IResult<&str, Vec<&str>> {
    let (remaining, message_or_newlines) =
        many0(alt((component::server_message, tag("\n"))))(input)?;
    Ok((remaining, message_or_newlines))
}

/// Parse an RPSL object from it's textual representation.
///
/// # Errors
/// Returns a Nom error if the input is not valid RPSL.
///
/// # Examples
/// ```
/// # use rpsl_parser::{parse_object, Attribute, Object};
/// # fn main() -> Result<(), nom::error::Error<&'static str>> {
/// let role_acme = "
/// role:        ACME Company
/// address:     Packet Street 6
/// address:     128 Series of Tubes
/// address:     Internet
/// email:       rpsl-parser@github.com
/// nic-hdl:     RPSL1-RIPE
/// source:      RIPE
///
/// ";
/// let object = parse_object(role_acme)?;
/// assert_eq!(
///     object,
///     Object::new(vec![
///         Attribute::new("role", "ACME Company"),
///         Attribute::new("address", "Packet Street 6"),
///         Attribute::new("address", "128 Series of Tubes"),
///         Attribute::new("address", "Internet"),
///         Attribute::new("email", "rpsl-parser@github.com"),
///         Attribute::new("nic-hdl", "RPSL1-RIPE"),
///         Attribute::new("source", "RIPE"),
///     ])
/// );
/// # Ok(())
/// # }
/// ```
///
/// Values spread over multiple lines can be parsed too.
/// ```
/// # use rpsl_parser::{parse_object, Attribute, Object};
/// # fn main() -> Result<(), nom::error::Error<&'static str>> {
/// let multiline_remark = "
/// remarks:     Value 1
///              Value 2
///
/// ";
/// assert_eq!(
///     parse_object(multiline_remark)?,
///     Object::new(vec![
///         Attribute::new("remarks", vec!["Value 1", "Value 2"])
///     ])
/// );
/// # Ok(())
/// # }
/// ```
///
/// An attribute that does not have a value is valid.
/// ```
/// # use rpsl_parser::{parse_object, Attribute, Object};
/// # fn main() -> Result<(), nom::error::Error<&'static str>> {
/// let without_value = "
/// as-name:     REMARKABLE
/// remarks:
/// remarks:     ^^^^^^^^^^ nothing here
///
/// ";
/// assert_eq!(
///     parse_object(without_value)?,
///     Object::new(vec![
///         Attribute::new("as-name", "REMARKABLE"),
///         Attribute::without_value("remarks"),
///         Attribute::new("remarks", "^^^^^^^^^^ nothing here"),
///     ])
/// );
/// # Ok(())
/// # }
/// ```
///
/// The same goes for values containing only whitespace.
/// Since whitespace to the left of a value is trimmed, they are equivalent to no value.
///
/// ```
/// # use rpsl_parser::{parse_object, Attribute, Object};
/// # fn main() -> Result<(), nom::error::Error<&'static str>> {
/// let whitespace_value = "
/// as-name:     REMARKABLE
/// remarks:               
/// remarks:     ^^^^^^^^^^ nothing but hot air
///
/// ";
/// assert_eq!(
///     parse_object(whitespace_value)?,
///     Object::new(vec![
///         Attribute::new("as-name", "REMARKABLE"),
///         Attribute::without_value("remarks"),
///         Attribute::new("remarks", "^^^^^^^^^^ nothing but hot air"),
///     ])
/// );
/// # Ok(())
/// # }
/// ```
pub fn parse_object(rpsl: &str) -> Result<Object, Error<&str>> {
    let (_, object) =
        all_consuming(delimited(multispace0, object_block, multispace0))(rpsl).finish()?;
    Ok(object)
}

/// Parse a whois server response containing multiple RPSL objects in their textual representation.
///
/// # Errors
/// Returns a Nom error if the input is not valid RPSL.
///
/// # Examples
/// ```
/// # use rpsl_parser::{parse_whois_response, Attribute, Object};
/// # fn main() -> Result<(), nom::error::Error<&'static str>> {
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
/// let objects: Vec<Object> = parse_whois_response(whois_response)?;
/// assert_eq!(
///     objects,
///     vec![
///             Object::new(vec![
///                 Attribute::new("ASNumber", "32934"),
///                 Attribute::new("ASName", "FACEBOOK"),
///                 Attribute::new("ASHandle", "AS32934"),
///                 Attribute::new("RegDate", "2004-08-24"),
///                 Attribute::new("Updated", "2012-02-24"),
///                 Attribute::new("Comment", "Please send abuse reports to abuse@facebook.com"),
///                 Attribute::new("Ref", "https://rdap.arin.net/registry/autnum/32934"),
///             ]),
///             Object::new(vec![
///                 Attribute::new("OrgName", "Facebook, Inc."),
///                 Attribute::new("OrgId", "THEFA-3"),
///                 Attribute::new("Address", "1601 Willow Rd."),
///                 Attribute::new("City", "Menlo Park"),
///                 Attribute::new("StateProv", "CA"),
///                 Attribute::new("PostalCode", "94025"),
///                 Attribute::new("Country", "US"),
///                 Attribute::new("RegDate", "2004-08-11"),
///                 Attribute::new("Updated", "2012-04-17"),
///                 Attribute::new("Ref", "https://rdap.arin.net/registry/entity/THEFA-3"),
///             ]),
///         ]
/// );
/// # Ok(())
/// # }
pub fn parse_whois_response(response: &str) -> Result<Vec<Object>, Error<&str>> {
    let (_, objects): (&str, Vec<Object>) =
        all_consuming(many1(padded_object_block))(response).finish()?;
    Ok(objects)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::Attribute;

    #[test]
    fn object_block_valid() {
        let object = concat!(
            "email:       rpsl-parser@github.com\n",
            "nic-hdl:     RPSL1-RIPE\n",
            "\n"
        );
        assert_eq!(
            object_block(object),
            Ok((
                "",
                Object::new(vec![
                    Attribute::new("email", "rpsl-parser@github.com").unwrap(),
                    Attribute::new("nic-hdl", "RPSL1-RIPE").unwrap()
                ])
            ))
        );
    }

    #[test]
    fn object_block_without_newline_termination_is_err() {
        let object = concat!(
            "email:       rpsl-parser@github.com\n",
            "nic-hdl:     RPSL1-RIPE\n",
        );
        assert!(object_block(object).is_err());
    }

    #[test]
    fn optional_comment_or_newlines_consumed() {
        assert_eq!(
            optional_message_or_newlines("% Note: This is a server message\n")
                .unwrap()
                .0,
            ""
        );
        assert_eq!(
            optional_message_or_newlines(concat!(
                "\n",
                "% Note: This is a server message followed by an empty line\n"
            ))
            .unwrap()
            .0,
            ""
        );
        assert_eq!(
            optional_message_or_newlines(concat!(
                "% Note: This is a server message preceeding some newlines.\n",
                "\n",
                "\n",
            ))
            .unwrap()
            .0,
            ""
        );
    }

    #[test]
    fn optional_comment_or_newlines_optional() {
        assert_eq!(
            optional_message_or_newlines(""),
            Ok(("", Vec::<&str>::new()))
        );
    }
}
