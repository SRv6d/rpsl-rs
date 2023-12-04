use super::Attribute;
use std::ops::Index;

/// An RPSL object.
///
/// ```text
/// ┌───────────────────────────────────────────────┐
/// │  Object                                       │
/// ├───────────────────────────────────────────────┤
/// │  [role]    ───  ACME Company                  │
/// │  [address] ──┬─ Packet Street 6               │
/// │              ├─ 128 Series of Tubes           │
/// │              └─ Internet                      │
/// │  [email]   ───  rpsl-parser@github.com        │
/// │  [nic-hdl] ───  RPSL1-RIPE                    │
/// │  [source]  ───  RIPE                          │
/// └───────────────────────────────────────────────┘
/// ```
///
/// # Examples
///
/// A role object for the ACME corporation.
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
///
/// /// Each attribute can be accessed by index.
/// ```
/// # use rpsl_parser::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role".parse()?, "ACME Company".parse()?),
/// #     Attribute::new("address".parse()?, "Packet Street 6".parse()?),
/// #     Attribute::new("address".parse()?, "128 Series of Tubes".parse()?),
/// #     Attribute::new("address".parse()?, "Internet".parse()?),
/// #     Attribute::new("email".parse()?, "rpsl-parser@github.com".parse()?),
/// #     Attribute::new("nic-hdl".parse()?, "RPSL1-RIPE".parse()?),
/// #     Attribute::new("source".parse()?, "RIPE".parse()?),
/// # ]);
/// assert_eq!(role_acme[0], Attribute::new("role".parse()?, "ACME Company".parse()?));
/// assert_eq!(role_acme[6], Attribute::new("source".parse()?, "RIPE".parse()?));
/// # Ok(())
/// # }
/// ```
///
/// While specific attribute values can be accessed by name.
/// ```
/// # use rpsl_parser::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role".parse()?, "ACME Company".parse()?),
/// #     Attribute::new("address".parse()?, "Packet Street 6".parse()?),
/// #     Attribute::new("address".parse()?, "128 Series of Tubes".parse()?),
/// #     Attribute::new("address".parse()?, "Internet".parse()?),
/// #     Attribute::new("email".parse()?, "rpsl-parser@github.com".parse()?),
/// #     Attribute::new("nic-hdl".parse()?, "RPSL1-RIPE".parse()?),
/// #     Attribute::new("source".parse()?, "RIPE".parse()?),
/// # ]);
/// assert_eq!(role_acme.get("role"), vec!["ACME Company"]);
/// assert_eq!(role_acme.get("address"), vec!["Packet Street 6", "128 Series of Tubes", "Internet"]);
/// assert_eq!(role_acme.get("email"), vec!["rpsl-parser@github.com"]);
/// assert_eq!(role_acme.get("nic-hdl"), vec!["RPSL1-RIPE"]);
/// assert_eq!(role_acme.get("source"), vec!["RIPE"]);
/// # Ok(())
/// # }
/// ```
///
/// The entire object can also be represented as RPSL.
/// ```
/// # use rpsl_parser::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role".parse()?, "ACME Company".parse()?),
/// #     Attribute::new("address".parse()?, "Packet Street 6".parse()?),
/// #     Attribute::new("address".parse()?, "128 Series of Tubes".parse()?),
/// #     Attribute::new("address".parse()?, "Internet".parse()?),
/// #     Attribute::new("email".parse()?, "rpsl-parser@github.com".parse()?),
/// #     Attribute::new("nic-hdl".parse()?, "RPSL1-RIPE".parse()?),
/// #     Attribute::new("source".parse()?, "RIPE".parse()?),
/// # ]);
/// assert_eq!(
///    role_acme.to_string(),
///    concat!(
///        "role:           ACME Company\n",
///        "address:        Packet Street 6\n",
///        "address:        128 Series of Tubes\n",
///        "address:        Internet\n",
///        "email:          rpsl-parser@github.com\n",
///        "nic-hdl:        RPSL1-RIPE\n",
///        "source:         RIPE\n",
///        "\n"
///    )
/// );
/// # Ok(())
/// # }
/// ```
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
