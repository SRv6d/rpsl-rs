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
