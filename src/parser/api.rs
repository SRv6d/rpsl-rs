use winnow::{
    ascii::multispace0,
    combinator::{delimited, repeat},
    Parser,
};

use super::core::{object_block, object_block_padded};
use crate::{Object, ParseError};

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
/// Returns a `ParseError` if the input is not valid RPSL.
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
pub fn parse_object(rpsl: &str) -> Result<Object, ParseError> {
    let block_parser = object_block();
    let object = delimited(multispace0, block_parser, multispace0).parse(rpsl)?;
    Ok(object)
}

/// Parse a WHOIS server response into [`Object`]s contained within.
///
/// # Errors
/// Returns a `ParseError` error if the input is not valid RPSL.
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
pub fn parse_whois_response(response: &str) -> Result<Vec<Object>, ParseError> {
    let block_parser = object_block_padded(object_block());
    let objects = repeat(1.., block_parser).parse(response)?;
    Ok(objects)
}
