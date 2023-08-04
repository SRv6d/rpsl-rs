use std::option::Option;

#[derive(Debug, PartialEq, Eq)]
pub struct Attribute {
    pub name: String,
    pub values: Vec<Option<String>>,
}

impl Attribute {
    pub fn new(name: String, values: Vec<Option<String>>) -> Self {
        Attribute { name, values }
    }
}

// Create an RPSL attribute from a tuple of slices parsed from RPSL text.
// An empty value or one containing only whitespace is converted to None.
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

#[derive(Debug, PartialEq, Eq)]
pub struct Object(Vec<Attribute>);

impl Object {
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

#[derive(Debug, PartialEq, Eq)]
pub struct ObjectCollection(Vec<Object>);

impl ObjectCollection {
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
