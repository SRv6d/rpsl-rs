use crate::rpsl::Attribute;

/// An RPSL object.
pub struct Object(Vec<Attribute>);

impl Object {
    /// Create a new RPSL object from a vector of attributes.
    fn new(attributes: Vec<Attribute>) -> Self {
        Object(attributes)
    }
}
