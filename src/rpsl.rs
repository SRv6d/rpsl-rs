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

#[derive(Debug, PartialEq, Eq)]
pub struct RpslObject(Vec<RpslAttribute>);

impl RpslObject {
    pub fn new(attributes: Vec<RpslAttribute>) -> Self {
        RpslObject(attributes)
    }

    // Create a RPSL object from a vector of tuples containing the attribute name and values.
    pub fn from_vec(attributes: Vec<(&str, Vec<&str>)>) -> Self {
        let mut converted: Vec<RpslAttribute> = Vec::with_capacity(attributes.len());

        for (name, values) in attributes {
            let attribute = RpslAttribute {
                name: name.to_string(),
                values: values.iter().map(|v| Some(v.to_string())).collect(),
            };

            converted.push(attribute);
        }

        RpslObject(converted)
    }
}

#[derive(Debug, PartialEq, Eq)]
pub struct RpslObjectCollection(Vec<RpslObject>);

impl RpslObjectCollection {
    pub fn new(objects: Vec<RpslObject>) -> Self {
        RpslObjectCollection(objects)
    }

    // Create an RPSL object collection from a vector of vectors of tuples containing the attribute name and values.
    pub fn from_vec(objects: Vec<Vec<(&str, Vec<&str>)>>) -> RpslObjectCollection {
        let mut converted: Vec<RpslObject> = Vec::with_capacity(objects.len());

        for object in objects {
            converted.push(RpslObject::from_vec(object));
        }
        RpslObjectCollection(converted)
    }
}
