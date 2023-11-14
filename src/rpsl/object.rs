use std::{fmt, ops::Index};

use crate::rpsl::Attribute;

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
///     Attribute::new("role", "ACME Company")?,
///     Attribute::new("address", "Packet Street 6")?,
///     Attribute::new("address", "128 Series of Tubes")?,
///     Attribute::new("address", "Internet")?,
///     Attribute::new("email", "rpsl-parser@github.com")?,
///     Attribute::new("nic-hdl", "RPSL1-RIPE")?,
///     Attribute::new("source", "RIPE")?,
/// ]);
/// # Ok(())
/// # }
/// ```
///
/// Each attribute can be accessed by index.
/// ```
/// # use rpsl_parser::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role", "ACME Company")?,
/// #     Attribute::new("address", "Packet Street 6")?,
/// #     Attribute::new("address", "128 Series of Tubes")?,
/// #     Attribute::new("address", "Internet")?,
/// #     Attribute::new("email", "rpsl-parser@github.com")?,
/// #     Attribute::new("nic-hdl", "RPSL1-RIPE")?,
/// #     Attribute::new("source", "RIPE")?,
/// # ]);
/// assert_eq!(role_acme[0], Attribute::new("role", "ACME Company")?);
/// assert_eq!(role_acme[6], Attribute::new("source", "RIPE")?);
/// # Ok(())
/// # }
/// ```
///
/// While specific attribute values can be accessed by name.
/// ```
/// # use rpsl_parser::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role", "ACME Company")?,
/// #     Attribute::new("address", "Packet Street 6")?,
/// #     Attribute::new("address", "128 Series of Tubes")?,
/// #     Attribute::new("address", "Internet")?,
/// #     Attribute::new("email", "rpsl-parser@github.com")?,
/// #     Attribute::new("nic-hdl", "RPSL1-RIPE")?,
/// #     Attribute::new("source", "RIPE")?,
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
/// #     Attribute::new("role", "ACME Company")?,
/// #     Attribute::new("address", "Packet Street 6")?,
/// #     Attribute::new("address", "128 Series of Tubes")?,
/// #     Attribute::new("address", "Internet")?,
/// #     Attribute::new("email", "rpsl-parser@github.com")?,
/// #     Attribute::new("nic-hdl", "RPSL1-RIPE")?,
/// #     Attribute::new("source", "RIPE")?,
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
#[derive(Debug, PartialEq, Eq)]
#[allow(clippy::len_without_is_empty)]
pub struct Object(Vec<Attribute>);

impl Object {
    /// Create a new RPSL object from a vector of attributes.
    #[must_use]
    pub fn new(attributes: Vec<Attribute>) -> Self {
        Object(attributes)
    }

    /// Returns the number of attributes in the object.
    #[must_use]
    pub fn len(&self) -> usize {
        self.0.len()
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

impl Index<usize> for Object {
    type Output = Attribute;

    fn index(&self, index: usize) -> &Self::Output {
        &self.0[index]
    }
}

impl IntoIterator for Object {
    type Item = Attribute;
    type IntoIter = std::vec::IntoIter<Attribute>;

    fn into_iter(self) -> Self::IntoIter {
        self.0.into_iter()
    }
}

impl From<Vec<Attribute>> for Object {
    fn from(attributes: Vec<Attribute>) -> Self {
        Self::new(attributes)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn values_by_name() {
        let as42 =
            Object::new(vec![
            Attribute::new("aut-num", "AS42").unwrap(),
            Attribute::new(
                "remarks",
                "All imported prefixes will be tagged with geographic communities and",
            ).unwrap(),
            Attribute::new(
                "remarks",
                "the type of peering relationship according to the table below, using the default",
            ).unwrap(),
            Attribute::new("remarks", "announce rule (x=0).").unwrap(),
            Attribute::new("remarks", "").unwrap(),
            Attribute::new(
                "remarks",
                "The following communities can be used by peers and customers",
            ).unwrap(),
            Attribute::new(
                "remarks",
                vec![
                    "x = 0 - Announce (default rule)",
                    "x = 1 - Prepend x1",
                    "x = 2 - Prepend x2",
                    "x = 3 - Prepend x3",
                    "x = 9 - Do not announce",
                ],
            ).unwrap(),
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
