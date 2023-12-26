use super::component;
use crate::ObjectView;
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
fn object_block(input: &str) -> IResult<&str, ObjectView> {
    let (remaining, attributes) = terminated(many1(component::attribute), newline)(input)?;
    Ok((remaining, ObjectView::new(attributes, Some(input))))
}

/// Uses the object block parser but allows for optional padding with server messages or newlines.
fn padded_object_block(input: &str) -> IResult<&str, ObjectView> {
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

/// Parse RPSL into an [`ObjectView`], a type that borrows from the RPSL input and provides
/// a convenient interface to access attributes as references.
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
/// role:           ACME Company ◀─────────────── &"role"    ───  &"ACME Company"
/// address:        Packet Street 6 ◀──────────── &"address" ───  &"Packet Street 6"
/// address:        128 Series of Tubes ◀──────── &"address" ───  &"128 Series of Tubes"
/// address:        Internet ◀─────────────────── &"address" ───  &"Internet"
/// email:          rpsl-rs@github.com ◀───── &"email"   ───  &"rpsl-rs@github.com"
/// nic-hdl:        RPSL1-RIPE ◀───────────────── &"nic-hdl" ───  &"RPSL1-RIPE"
/// source:         RIPE ◀─────────────────────── &"source"  ───  &"RIPE"

/// ```
///
/// # Errors
/// Returns a Nom error if the input is not valid RPSL.
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
/// remarks:     ^^^^^^^^^^ nothing but hot air
///
/// ";
/// assert_eq!(
///     parse_object(whitespace_value)?,
///     object! {
///         "as-name": "REMARKABLE";
///         "remarks": "";
///         "remarks": "^^^^^^^^^^ nothing but hot air";
///     }
/// );
/// # Ok(())
/// # }
/// ```
pub fn parse_object(rpsl: &str) -> Result<ObjectView, Error<&str>> {
    let (_, object) =
        all_consuming(delimited(multispace0, object_block, multispace0))(rpsl).finish()?;
    Ok(object)
}

/// Parse a WHOIS server response into [`ObjectView`]s of the objects contained within.
///
/// # Errors
/// Returns a Nom error if the input is not valid RPSL.
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
pub fn parse_whois_response(response: &str) -> Result<Vec<ObjectView>, Error<&str>> {
    let (_, objects): (&str, Vec<ObjectView>) =
        all_consuming(many1(padded_object_block))(response).finish()?;
    Ok(objects)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::{AttributeView, ObjectView};

    #[test]
    fn object_block_valid() {
        let object = concat!(
            "email:       rpsl-rs@github.com\n",
            "nic-hdl:     RPSL1-RIPE\n",
            "\n"
        );
        assert_eq!(
            object_block(object),
            Ok((
                "",
                ObjectView::new(
                    vec![
                        AttributeView::new_single("email", "rpsl-rs@github.com"),
                        AttributeView::new_single("nic-hdl", "RPSL1-RIPE")
                    ],
                    Some(object)
                )
            ))
        );
    }

    #[test]
    fn object_block_without_newline_termination_is_err() {
        let object = concat!(
            "email:       rpsl-rs@github.com\n",
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
                "% Note: This is a server message preceding some newlines.\n",
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
