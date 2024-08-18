use super::attribute::Attribute;
use std::{
    fmt,
    ops::{Deref, Index},
};

/// A RPSL object.
///
/// ```text
/// ┌───────────────────────────────────────────────┐
/// │  Object                                       │
/// ├───────────────────────────────────────────────┤
/// │  [role]    ───  ACME Company                  │
/// │  [address] ──┬─ Packet Street 6               │
/// │              ├─ 128 Series of Tubes           │
/// │              └─ Internet                      │
/// │  [email]   ───  rpsl-rs@github.com            │
/// │  [nic-hdl] ───  RPSL1-RIPE                    │
/// │  [source]  ───  RIPE                          │
/// └───────────────────────────────────────────────┘
/// ```
///
/// # Examples
///
/// A role object for the ACME corporation.
/// ```
/// # use rpsl::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let role_acme = Object::new(vec![
///     Attribute::new("role".parse()?, "ACME Company".parse()?),
///     Attribute::new("address".parse()?, "Packet Street 6".parse()?),
///     Attribute::new("address".parse()?, "128 Series of Tubes".parse()?),
///     Attribute::new("address".parse()?, "Internet".parse()?),
///     Attribute::new("email".parse()?, "rpsl-rs@github.com".parse()?),
///     Attribute::new("nic-hdl".parse()?, "RPSL1-RIPE".parse()?),
///     Attribute::new("source".parse()?, "RIPE".parse()?),
/// ]);
/// # Ok(())
/// # }
/// ```
///
/// Although creating an [`Object`] from a vector of [`Attribute`]s works, the more idiomatic way
/// to do it is by using the [`object!`](crate::object) macro.
/// ```
/// # use rpsl::{Attribute, Object, object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role".parse()?, "ACME Company".parse()?),
/// #     Attribute::new("address".parse()?, "Packet Street 6".parse()?),
/// #     Attribute::new("address".parse()?, "128 Series of Tubes".parse()?),
/// #     Attribute::new("address".parse()?, "Internet".parse()?),
/// #     Attribute::new("email".parse()?, "rpsl-rs@github.com".parse()?),
/// #     Attribute::new("nic-hdl".parse()?, "RPSL1-RIPE".parse()?),
/// #     Attribute::new("source".parse()?, "RIPE".parse()?),
/// # ]);
/// assert_eq!(
///     role_acme,
///     object! {
///         "role": "ACME Company";
///         "address": "Packet Street 6";
///         "address": "128 Series of Tubes";
///         "address": "Internet";
///         "email": "rpsl-rs@github.com";
///         "nic-hdl": "RPSL1-RIPE";
///         "source": "RIPE";
///     },
/// );
/// # Ok(())
/// # }
/// ```
///
/// Each attribute can be accessed by index.
/// ```
/// # use rpsl::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role".parse()?, "ACME Company".parse()?),
/// #     Attribute::new("address".parse()?, "Packet Street 6".parse()?),
/// #     Attribute::new("address".parse()?, "128 Series of Tubes".parse()?),
/// #     Attribute::new("address".parse()?, "Internet".parse()?),
/// #     Attribute::new("email".parse()?, "rpsl-rs@github.com".parse()?),
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
/// # use rpsl::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role".parse()?, "ACME Company".parse()?),
/// #     Attribute::new("address".parse()?, "Packet Street 6".parse()?),
/// #     Attribute::new("address".parse()?, "128 Series of Tubes".parse()?),
/// #     Attribute::new("address".parse()?, "Internet".parse()?),
/// #     Attribute::new("email".parse()?, "rpsl-rs@github.com".parse()?),
/// #     Attribute::new("nic-hdl".parse()?, "RPSL1-RIPE".parse()?),
/// #     Attribute::new("source".parse()?, "RIPE".parse()?),
/// # ]);
/// assert_eq!(role_acme.get("role"), vec!["ACME Company"]);
/// assert_eq!(role_acme.get("address"), vec!["Packet Street 6", "128 Series of Tubes", "Internet"]);
/// assert_eq!(role_acme.get("email"), vec!["rpsl-rs@github.com"]);
/// assert_eq!(role_acme.get("nic-hdl"), vec!["RPSL1-RIPE"]);
/// assert_eq!(role_acme.get("source"), vec!["RIPE"]);
/// # Ok(())
/// # }
/// ```
///
/// The entire object can also be represented as RPSL.
/// ```
/// # use rpsl::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role".parse()?, "ACME Company".parse()?),
/// #     Attribute::new("address".parse()?, "Packet Street 6".parse()?),
/// #     Attribute::new("address".parse()?, "128 Series of Tubes".parse()?),
/// #     Attribute::new("address".parse()?, "Internet".parse()?),
/// #     Attribute::new("email".parse()?, "rpsl-rs@github.com".parse()?),
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
///        "email:          rpsl-rs@github.com\n",
///        "nic-hdl:        RPSL1-RIPE\n",
///        "source:         RIPE\n",
///        "\n"
///    )
/// );
/// # Ok(())
/// # }
/// ```
#[derive(Debug, PartialEq, Eq, Clone)]
#[allow(clippy::len_without_is_empty)]
pub struct Object<'a> {
    attributes: Vec<Attribute<'a>>,
    /// Contains the source if the object was created by parsing RPSL.
    source: Option<&'a str>,
}

impl Object<'_> {
    /// Create a new RPSL object from a vector of attributes.
    ///
    /// # Example
    /// ```
    /// # use rpsl::{Attribute, Object};
    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
    /// let role_acme = Object::new(vec![
    ///     Attribute::new("role".parse()?, "ACME Company".parse()?),
    ///     Attribute::new("address".parse()?, "Packet Street 6".parse()?),
    ///     Attribute::new("address".parse()?, "128 Series of Tubes".parse()?),
    ///     Attribute::new("address".parse()?, "Internet".parse()?),
    ///     Attribute::new("email".parse()?, "rpsl-rs@github.com".parse()?),
    ///     Attribute::new("nic-hdl".parse()?, "RPSL1-RIPE".parse()?),
    ///     Attribute::new("source".parse()?, "RIPE".parse()?),
    /// ]);
    /// # Ok(())
    /// # }
    /// ```
    #[must_use]
    pub fn new(attributes: Vec<Attribute<'static>>) -> Object<'static> {
        Object {
            attributes,
            source: None,
        }
    }

    pub(crate) fn from_parsed<'a>(attributes: Vec<Attribute<'a>>, source: &'a str) -> Object<'a> {
        Object {
            attributes,
            source: Some(source),
        }
    }

    /// The number of attributes in the object.
    #[must_use]
    pub fn len(&self) -> usize {
        self.attributes.len()
    }

    /// Get the value(s) of specific attribute(s).
    #[must_use]
    pub fn get(&self, name: &str) -> Vec<&str> {
        self.attributes
            .iter()
            .filter(|a| a.name == name)
            .flat_map(|a| a.value.with_content())
            .collect()
    }
}

impl<'a> Index<usize> for Object<'a> {
    type Output = Attribute<'a>;

    fn index(&self, index: usize) -> &Self::Output {
        &self.attributes[index]
    }
}

impl<'a> Deref for Object<'a> {
    type Target = Vec<Attribute<'a>>;

    fn deref(&self) -> &Self::Target {
        &self.attributes
    }
}

impl<'a> IntoIterator for Object<'a> {
    type Item = Attribute<'a>;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        self.attributes.into_iter()
    }
}

impl fmt::Display for Object<'_> {
    /// Display the object as RPSL.
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for attribute in &self.attributes {
            write!(f, "{attribute}")?;
        }
        writeln!(f)
    }
}

/// Creates an [`Object`] containing the given attributes.
///
/// - Create an [`Object`] containing only single value attributes:
/// ```
/// # use rpsl::object;
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let obj = object! {
///     "role": "ACME Company";
///     "address": "Packet Street 6";
///     "address": "128 Series of Tubes";
///     "address": "Internet";
/// };
/// assert_eq!(obj[0].name, "role");
/// assert_eq!(obj[0].value, "ACME Company");
/// assert_eq!(obj[1].name, "address");
/// assert_eq!(obj[1].value, "Packet Street 6");
/// assert_eq!(obj[2].name, "address");
/// assert_eq!(obj[2].value, "128 Series of Tubes");
/// assert_eq!(obj[3].name, "address");
/// assert_eq!(obj[3].value, "Internet");
/// # Ok(())
/// # }
/// ```
///
/// - Create an `Object` containing multi value attributes:
/// ```
/// # use rpsl::object;
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let obj = object! {
///    "role": "ACME Company";
///    "address": "Packet Street 6", "128 Series of Tubes", "Internet";
/// };
/// assert_eq!(obj[0].name, "role");
/// assert_eq!(obj[0].value, "ACME Company");
/// assert_eq!(obj[1].name, "address");
/// assert_eq!(obj[1].value, vec!["Packet Street 6", "128 Series of Tubes", "Internet"]);
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
