use std::option::Option;

#[derive(Debug, PartialEq, Eq)]
pub struct RpslAttribute {
    pub name: String,
    pub values: Vec<Option<String>>,
}

impl RpslAttribute {
    pub fn new(name: String, values: Vec<Option<String>>) -> Self {
        RpslAttribute { name, values }
    }
}

// Create an RPSL attribute from a tuple of slices parsed from RPSL text.
impl From<(&str, Vec<&str>)> for RpslAttribute {
    fn from(attribute_slice: (&str, Vec<&str>)) -> Self {
        let (name, values) = attribute_slice;

        let attribute = RpslAttribute {
            name: name.to_string(),
            values: values.iter().map(|v| Some(v.to_string())).collect(),
        };

        attribute
    }
}

#[derive(Debug, PartialEq, Eq)]
pub struct RpslObject(Vec<RpslAttribute>);

impl RpslObject {
    pub fn new(attributes: Vec<RpslAttribute>) -> Self {
        RpslObject(attributes)
    }
}

// Create an RPSL object from a vector of slices parsed from RPSL text.
impl From<Vec<(&str, Vec<&str>)>> for RpslObject {
    fn from(attribute_slices: Vec<(&str, Vec<&str>)>) -> Self {
        let mut attributes: Vec<RpslAttribute> = Vec::with_capacity(attribute_slices.len());

        for attribute_slice in attribute_slices {
            attributes.push(RpslAttribute::from(attribute_slice));
        }

        RpslObject(attributes)
    }
}

#[derive(Debug, PartialEq, Eq)]
pub struct RpslObjectCollection(Vec<RpslObject>);

impl RpslObjectCollection {
    pub fn new(objects: Vec<RpslObject>) -> Self {
        RpslObjectCollection(objects)
    }
}

// Create an RPSL object collection from a vector of slices parsed from RPSL text.
impl From<Vec<Vec<(&str, Vec<&str>)>>> for RpslObjectCollection {
    fn from(object_slices: Vec<Vec<(&str, Vec<&str>)>>) -> Self {
        let mut objects: Vec<RpslObject> = Vec::with_capacity(object_slices.len());

        for object in object_slices {
            objects.push(RpslObject::from(object));
        }

        RpslObjectCollection(objects)
    }
}
