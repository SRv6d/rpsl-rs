use crate::rpsl::Attribute;

/// An RPSL object.
#[derive(Debug, PartialEq, Eq)]
pub struct Object(Vec<Attribute>);

impl Object {
    /// Create a new RPSL object from a vector of attributes.
    pub fn new(attributes: Vec<Attribute>) -> Self {
        Object(attributes)
    }
}

impl From<Vec<Attribute>> for Object {
    fn from(attributes: Vec<Attribute>) -> Self {
        Self::new(attributes)
    }
}
