use super::component;
use crate::{Attribute, Object};
use winnow::{
    ascii::{multispace0, newline},
    combinator::{delimited, repeat, terminated, todo},
    PResult, Parser,
};

/// Parse an object with at least one attribute terminated by a newline.
///
/// As per [RFC 2622](https://datatracker.ietf.org/doc/html/rfc2622#section-2), an RPSL object
/// is textually represented as a list of attribute-value pairs that ends when a blank line is encountered.
fn object_block<'s>(input: &mut &'s str) -> PResult<Object<'s>> {
    let attributes: Vec<Attribute> =
        terminated(repeat(1.., component::attribute), newline).parse_next(input)?;
    Ok(Object::from_parsed(input, attributes))
}

/// Uses the object block parser but allows for optional padding with server messages or newlines.
fn padded_object_block<'s>(input: &mut &'s str) -> PResult<Object<'s>> {
    todo.parse_next(input)
}

/// Consume an unlimited number of optional server messages or newlines.
fn optional_message_or_newlines(input: &mut &str) -> PResult<()> {
    todo!()
}

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
/// role:           ACME Company ◀─────────────── &"role"    ───  &"ACME Company"
/// address:        Packet Street 6 ◀──────────── &"address" ───  &"Packet Street 6"
/// address:        128 Series of Tubes ◀──────── &"address" ───  &"128 Series of Tubes"
/// address:        Internet ◀─────────────────── &"address" ───  &"Internet"
/// email:          rpsl-rs@github.com ◀───────── &"email"   ───  &"rpsl-rs@github.com"
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
pub fn parse_object(rpsl: &str) -> Result<Object, ()> {
    let object = delimited(multispace0, object_block, multispace0)
        .parse(rpsl)
        .unwrap();
    Ok(object)
}

/// Parse a WHOIS server response into [`Object`]s contained within.
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
pub fn parse_whois_response(response: &str) -> Result<Vec<Object>, ()> {
    let objects = repeat(1.., padded_object_block).parse(response).unwrap();
    Ok(objects)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::{Attribute, Object};
    use rstest::*;

    #[test]
    fn object_block_valid() {
        let object = &mut concat!(
            "email:       rpsl-rs@github.com\n",
            "nic-hdl:     RPSL1-RIPE\n",
            "\n"
        );
        assert_eq!(
            object_block(object),
            Ok(Object::from_parsed(
                object,
                vec![
                    Attribute::unchecked_single("email", "rpsl-rs@github.com"),
                    Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE")
                ]
            ))
        );
    }

    #[test]
    fn object_block_without_newline_termination_is_err() {
        let object = &mut concat!(
            "email:       rpsl-rs@github.com\n",
            "nic-hdl:     RPSL1-RIPE\n",
        );
        assert!(object_block(object).is_err());
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
        optional_message_or_newlines(given).unwrap();
        assert_eq!(*given, "");
    }

    #[test]
    fn optional_comment_or_newlines_optional() {
        assert_eq!(optional_message_or_newlines(&mut ""), Ok(()));
    }
}
