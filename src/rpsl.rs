use std::option::Option;

#[derive(Debug)]
pub enum RpslAttribute {
    SingleValue,
    MultiValue,
}

#[derive(Debug)]
struct SingleValue {
    name: String,
    value: Option<String>,
}

#[derive(Debug)]
struct MultiValue {
    name: String,
    values: Vec<Option<String>>,
}

pub type RpslObject = Vec<RpslAttribute>;

pub type RpslObjectCollection = Vec<RpslObject>;
