use std::ops::Index;

use crate::rpsl::Attribute;

/// An RPSL object.
///
/// # Examples
///
/// A role object for the ACME corporation.
/// ```
/// # use rpsl_parser::{Attribute, Object};
/// let role_acme = Object::new(vec![
///     Attribute::new("role", "ACME Company"),
///     Attribute::new("address", "Packet Street 6"),
///     Attribute::new("address", "128 Series of Tubes"),
///     Attribute::new("address", "Internet"),
///     Attribute::new("email", "rpsl-parser@github.com"),
///     Attribute::new("nic-hdl", "RPSL1-RIPE"),
///     Attribute::new("source", "RIPE"),
/// ]);
/// ```
///
/// Each attribute can be accessed by index.
/// ```
/// # use rpsl_parser::{Attribute, Object};
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role", "ACME Company"),
/// #     Attribute::new("address", "Packet Street 6"),
/// #     Attribute::new("address", "128 Series of Tubes"),
/// #     Attribute::new("address", "Internet"),
/// #     Attribute::new("email", "rpsl-parser@github.com"),
/// #     Attribute::new("nic-hdl", "RPSL1-RIPE"),
/// #     Attribute::new("source", "RIPE"),
/// # ]);
/// assert_eq!(role_acme[0], Attribute::new("role", "ACME Company"));
/// assert_eq!(role_acme[6], Attribute::new("source", "RIPE"));
/// ```
///
/// The entire object can also be represented as RPSL.
/// ```
/// # use rpsl_parser::{Attribute, Object};
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role", "ACME Company"),
/// #     Attribute::new("address", "Packet Street 6"),
/// #     Attribute::new("address", "128 Series of Tubes"),
/// #     Attribute::new("address", "Internet"),
/// #     Attribute::new("email", "rpsl-parser@github.com"),
/// #     Attribute::new("nic-hdl", "RPSL1-RIPE"),
/// #     Attribute::new("source", "RIPE"),
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
#[derive(Debug, PartialEq, Eq)]
pub struct Object(Vec<Attribute>);

impl Object {
    /// Create a new RPSL object from a vector of attributes.
    pub fn new(attributes: Vec<Attribute>) -> Self {
        Object(attributes)
    }

    /// Returns the number of attributes in the object.
    pub fn len(&self) -> usize {
        self.0.len()
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
