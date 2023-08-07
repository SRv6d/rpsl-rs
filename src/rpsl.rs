//! Types for representing RPSL components.
use std::option::Option;

/// Represents a RPSL attribute.
#[derive(Debug, PartialEq, Eq)]
pub struct Attribute {
    /// The name of the attribute.
    pub name: String,
    /// The values of the attribute.
    /// Single line attributes only have one value, while for multi-line attributes every line is a value.
    /// An empty value or one containing only whitespace is represented as None.
    pub values: Vec<Option<String>>,
}

impl Attribute {
    /// Create a new RPSL attribute from a name and vector of values.
    pub fn new(name: String, values: Vec<Option<String>>) -> Self {
        Attribute { name, values }
    }
}

/// Create a RPSL attribute from a tuple of slices parsed from RPSL text.
/// An empty value or one containing only whitespace is converted to None.
impl From<(&str, Vec<&str>)> for Attribute {
    fn from(attribute_slice: (&str, Vec<&str>)) -> Self {
        let (name, values) = attribute_slice;

        Attribute {
            name: name.to_string(),
            values: values
                .iter()
                .map(|v| {
                    if v.trim().is_empty() {
                        return None;
                    }
                    Some((*v).to_string())
                })
                .collect(),
        }
    }
}

/// Represents a RPSL object.
#[derive(Debug, PartialEq, Eq)]
pub struct Object(Vec<Attribute>);

impl Object {
    /// Create a new RPSL object from a vector of attributes.
    pub fn new(attributes: Vec<Attribute>) -> Self {
        Object(attributes)
    }
}

impl IntoIterator for Object {
    type Item = Attribute;
    type IntoIter = std::vec::IntoIter<Attribute>;

    fn into_iter(self) -> Self::IntoIter {
        self.0.into_iter()
    }
}

// Create an RPSL object from a vector of slices parsed from RPSL text.
impl From<Vec<(&str, Vec<&str>)>> for Object {
    fn from(attribute_slices: Vec<(&str, Vec<&str>)>) -> Self {
        let mut attributes: Vec<Attribute> = Vec::with_capacity(attribute_slices.len());

        for attribute_slice in attribute_slices {
            attributes.push(Attribute::from(attribute_slice));
        }

        Object(attributes)
    }
}
///Represents a collection of RPSL objects, for example as the result of a whois query.
#[derive(Debug, PartialEq, Eq)]
pub struct ObjectCollection(Vec<Object>);

impl ObjectCollection {
    /// Create a new RPSL object collection from a vector of objects.
    pub fn new(objects: Vec<Object>) -> Self {
        ObjectCollection(objects)
    }
}

impl IntoIterator for ObjectCollection {
    type Item = Object;
    type IntoIter = std::vec::IntoIter<Object>;

    fn into_iter(self) -> Self::IntoIter {
        self.0.into_iter()
    }
}

// Create an RPSL object collection from a vector of slices parsed from RPSL text.
impl From<Vec<Vec<(&str, Vec<&str>)>>> for ObjectCollection {
    fn from(object_slices: Vec<Vec<(&str, Vec<&str>)>>) -> Self {
        let mut objects: Vec<Object> = Vec::with_capacity(object_slices.len());

        for object in object_slices {
            objects.push(Object::from(object));
        }

        ObjectCollection(objects)
    }
}
