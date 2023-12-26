use super::Attribute;
use std::{fmt, ops::Index};

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
pub struct Object(Vec<Attribute>);

impl Object {
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
    pub fn new(attributes: Vec<Attribute>) -> Self {
        Object(attributes)
    }

    /// The number of attributes in the object.
    #[must_use]
    pub fn len(&self) -> usize {
        self.0.len()
    }

    /// Get the value(s) of specific attribute(s).
    pub fn get(&self, name: &str) -> Vec<&String> {
        let values_matching_name = self.0.iter().filter(|a| a.name == name).map(|a| &a.value);

        let mut values: Vec<&String> = Vec::new();
        for value in values_matching_name {
            match value {
                super::attribute::Value::SingleLine(ref v) => {
                    if let Some(v) = v.as_ref() {
                        values.push(v);
                    }
                }
                super::attribute::Value::MultiLine(ref v) => {
                    values.extend(v.iter().filter_map(Option::as_ref));
                }
            }
        }
        values
    }
}

impl Index<usize> for Object {
    type Output = Attribute;

    fn index(&self, index: usize) -> &Self::Output {
        &self.0[index]
    }
}

impl IntoIterator for Object {
    type Item = Attribute;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        self.0.into_iter()
    }
}

impl fmt::Display for Object {
    /// Display the object as RPSL.
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for attribute in &self.0 {
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn object_from_macro() {
        let object = object! {
            "role": "ACME Company";
            "address": "Packet Street 6", "128 Series of Tubes", "Internet";
            "email": "rpsl-rs@github.com";
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
                "rpsl-rs@github.com".parse().unwrap(),
            ),
            Attribute::new("nic-hdl".parse().unwrap(), "RPSL1-RIPE".parse().unwrap()),
            Attribute::new("source".parse().unwrap(), "RIPE".parse().unwrap()),
        ]);
        assert_eq!(object, role_acme);
    }

    #[test]
    fn values_by_name() {
        let as42 =
            Object::new(vec![
            Attribute::new("aut-num".parse().unwrap(), "AS42".parse().unwrap()),
            Attribute::new(
                "remarks".parse().unwrap(),
                "All imported prefixes will be tagged with geographic communities and"
                    .parse()
                    .unwrap(),
            ),
            Attribute::new(
                "remarks".parse().unwrap(),
                "the type of peering relationship according to the table below, using the default"
                    .parse()
                    .unwrap(),
            ),
            Attribute::new(
                "remarks".parse().unwrap(),
                "announce rule (x=0).".parse().unwrap(),
            ),
            Attribute::new("remarks".parse().unwrap(), "".parse().unwrap()),
            Attribute::new(
                "remarks".parse().unwrap(),
                "The following communities can be used by peers and customers".parse().unwrap(),
            ),
            Attribute::new(
                "remarks".parse().unwrap(),
                vec![
                    "x = 0 - Announce (default rule)",
                    "x = 1 - Prepend x1",
                    "x = 2 - Prepend x2",
                    "x = 3 - Prepend x3",
                    "x = 9 - Do not announce",
                ].try_into().unwrap(),
            ),
        ]);
        assert_eq!(as42.get("aut-num"), vec!["AS42"]);
        assert_eq!(
            as42.get("remarks"),
            vec![
                "All imported prefixes will be tagged with geographic communities and",
                "the type of peering relationship according to the table below, using the default",
                "announce rule (x=0).",
                "The following communities can be used by peers and customers",
                "x = 0 - Announce (default rule)",
                "x = 1 - Prepend x1",
                "x = 2 - Prepend x2",
                "x = 3 - Prepend x3",
                "x = 9 - Do not announce",
            ]
        );
    }
}
