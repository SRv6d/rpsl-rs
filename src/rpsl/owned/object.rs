use super::Attribute;
use std::ops::Index;

/// An RPSL object.
#[derive(Debug, PartialEq, Eq, Clone)]
pub struct Object(Vec<Attribute>);

impl Object {
    /// Create a new RPSL object from a vector of attributes.
    ///
    /// # Example
    /// ```
    /// # use rpsl_parser::{Attribute, Object};
    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
    /// let role_acme = Object::new(vec![
    ///     Attribute::new("role".parse()?, "ACME Company".parse()?),
    ///     Attribute::new("address".parse()?, "Packet Street 6".parse()?),
    ///     Attribute::new("address".parse()?, "128 Series of Tubes".parse()?),
    ///     Attribute::new("address".parse()?, "Internet".parse()?),
    ///     Attribute::new("email".parse()?, "rpsl-parser@github.com".parse()?),
    ///     Attribute::new("nic-hdl".parse()?, "RPSL1-RIPE".parse()?),
    ///     Attribute::new("source".parse()?, "RIPE".parse()?),
    /// ]);
    /// # Ok(())
    /// # }
    /// ```
    #[must_use]
    pub fn new(attributes: Vec<Attribute>) -> Self {
        Object(attributes)
    }
}

impl Index<usize> for Object {
    type Output = Attribute;

    fn index(&self, index: usize) -> &Self::Output {
        &self.0[index]
    }
}

/// Creates an [`Object`] containing the given attributes.
///
/// - Create an [`Object`] containing only single value attributes:
/// ```
/// # use rpsl_parser::object;
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let obj = object! {
///     "role": "ACME Company";
///     "address": "Packet Street 6";
///     "address": "128 Series of Tubes";
///     "address": "Internet";
/// };
/// assert_eq!(obj[0].name, "role".parse()?);
/// assert_eq!(obj[0].value, "ACME Company".parse()?);
/// assert_eq!(obj[1].name, "address".parse()?);
/// assert_eq!(obj[1].value, "Packet Street 6".parse()?);
/// assert_eq!(obj[2].name, "address".parse()?);
/// assert_eq!(obj[2].value, "128 Series of Tubes".parse()?);
/// assert_eq!(obj[3].name, "address".parse()?);
/// assert_eq!(obj[3].value, "Internet".parse()?);
/// # Ok(())
/// # }
/// ```
///
/// - Create an `Object` containing multi value attributes:
/// ```
/// # use rpsl_parser::object;
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let obj = object! {
///    "role": "ACME Company";
///    "address": "Packet Street 6", "128 Series of Tubes", "Internet";
/// };
/// assert_eq!(obj[0].name, "role".parse()?);
/// assert_eq!(obj[0].value, "ACME Company".parse()?);
/// assert_eq!(obj[1].name, "address".parse()?);
/// assert_eq!(obj[1].value, vec!["Packet Street 6", "128 Series of Tubes", "Internet"].try_into()?);
/// # Ok(())
/// # }
#[macro_export]
macro_rules! object {
    (
        $(
            $name:literal: $($value:literal),+
        );+ $(;)?
    ) => {
        $crate::Object::new(vec![
            $(
                $crate::Attribute::new($name.parse().unwrap(), vec![$($value),+].try_into().unwrap()),
            )*
        ])
    };
}

mod tests {
    use super::*;

    #[test]
    fn object_from_macro() {
        let object = object! {
            "role": "ACME Company";
            "address": "Packet Street 6", "128 Series of Tubes", "Internet";
            "email": "rpsl-parser@github.com";
            "nic-hdl": "RPSL1-RIPE";
            "source": "RIPE";
        };
        let role_acme = Object::new(vec![
            Attribute::new("role".parse().unwrap(), "ACME Company".parse().unwrap()),
            Attribute::new(
                "address".parse().unwrap(),
                vec!["Packet Street 6", "128 Series of Tubes", "Internet"]
                    .try_into()
                    .unwrap(),
            ),
            Attribute::new(
                "email".parse().unwrap(),
                "rpsl-parser@github.com".parse().unwrap(),
            ),
            Attribute::new("nic-hdl".parse().unwrap(), "RPSL1-RIPE".parse().unwrap()),
            Attribute::new("source".parse().unwrap(), "RIPE".parse().unwrap()),
        ]);
        assert_eq!(object, role_acme);
    }
}
