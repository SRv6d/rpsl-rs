use super::component;
use crate::rpsl::{Attribute, Object};
use nom::{
    character::complete::multispace0, combinator::all_consuming, error::Error, multi::many1,
    sequence::delimited, Finish, IResult,
};

/// Parse a string containing one or more attributes into a vector of attributes.
///
/// # Example
/// ```
/// # use rpsl::parser::main::many1_attributes;
/// # use rpsl::rpsl::Attribute;
///
/// let attributes = "
/// email:       rpsl-parser@github.com
/// nic-hdl:     RPSL1-RIPE
/// "
/// assert_eq!(
///     many1_attributes(attributes),
///     Ok((
///         "",
///         vec![
///             Attribute::new("email", "rpsl-parser@github.com"),
///             Attribute::new("nic-hdl", "RPSL1-RIPE")
///         ]
///     ))
/// );
pub(crate) fn many1_attributes(input: &str) -> IResult<&str, Vec<Attribute>> {
    let (remaining, attributes) = many1(component::attribute)(input)?;
    Ok((remaining, attributes))
}

/// Parse an RPSL object from it's textual representation.
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
/// ";
/// let object = parse_object(role_acme)?;
/// assert_eq!(
///     object,
///     Object::new(vec![
///         Attribute::new("role" "ACME Company"),
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
/// Empty values are valid and are represented as `None`.
/// ```
/// # use rpsl_parser::{parse_object, Attribute, Object};
/// # fn main() -> Result<(), nom::error::Error<&'static str>> {
/// let empty_value = "
/// as-name:     REMARKABLE
/// remarks:
/// remarks:     ^^^^^^^^^^ nothing here
/// ";
/// assert_eq!(
///     parse_rpsl_object(empty_value)?,
///     Object::new(vec![
///         Attribute::new("as-name", "REMARKABLE"),
///         Attribute::new("remarks", None),
///         Attribute::new("remarks", "^^^^^^^^^^ nothing here"),
///     ])
/// );
/// # Ok(())
/// # }
/// ```
///
/// The same goes for values containing only whitespace.
/// Since whitespace to the left of a value is trimmed, they are equivalent to an empty value.
///
/// ```
/// # use rpsl_parser::{parse_rpsl_object, rpsl};
/// # fn main() -> Result<(), nom::error::Error<&'static str>> {
/// let whitespace_value = "
/// as-name:     REMARKABLE
/// remarks:               
/// remarks:     ^^^^^^^^^^ nothing but hot air
/// ";
/// assert_eq!(
///     parse_rpsl_object(whitespace_value)?,
///     Object::new(vec![
///         Attribute::new("as-name", "REMARKABLE"),
///         Attribute::new("remarks", None),
///         Attribute::new("remarks", "^^^^^^^^^^ nothing but hot air"),
///     ])
/// );
/// # Ok(())
/// # }
/// ```
pub fn parse_object(rpsl: &str) -> Result<Object, Error<&str>> {
    let (_, attributes) =
        all_consuming(delimited(multispace0, many1_attributes, multispace0))(rpsl).finish()?;
    Ok(Object::new(attributes))
}

/// Parse a whois server response contaning multiple RPSL objects in their textual representation.
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
    ()
}
