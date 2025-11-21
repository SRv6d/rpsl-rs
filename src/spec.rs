use super::attribute::{Attribute, Name, Value};
use std::fmt::Debug;

pub trait Specification: Debug + Clone + Copy {
    fn validate_attribute<S: Specification>(
        attribute: &Attribute<'_, S>,
    ) -> Result<(), AttributeError>;
}

#[derive(Debug, Default, Clone, Copy, PartialEq, Eq)]
pub struct Raw;

impl Specification for Raw {
    fn validate_attribute<S: Specification>(
        _attribute: &Attribute<'_, S>,
    ) -> Result<(), AttributeError> {
        Ok(())
    }
}

#[derive(Debug, Default, Clone, Copy, PartialEq, Eq)]
pub struct Rfc2622;

impl Specification for Rfc2622 {
    fn validate_attribute<S: Specification>(
        _attribute: &Attribute<'_, S>,
    ) -> Result<(), AttributeError> {
        todo!()
    }
}

#[derive(thiserror::Error, Debug)]
/// An invalid attribute was encountered during validation.
pub enum AttributeError {
    /// The name of the attribute is invalid.
    #[error("invalid attribute name {0}")]
    InvalidName(#[from] InvalidNameError),
    /// The value of the attribute is invalid.
    #[error("invalid attribute value {0}")]
    InvalidValue(#[from] InvalidValueError),
}

/// The attribute has an invalid name.
#[derive(thiserror::Error, Debug)]
#[error("`{name}`: {message}")]
pub struct InvalidNameError {
    name: Name<'static>,
    message: String,
}

impl InvalidNameError {
    fn new(name: &Name, message: String) -> Self {
        Self {
            name: name.clone().into_owned(),
            message,
        }
    }
}

/// The attribute has an invalid value.
#[derive(thiserror::Error, Debug)]
#[error("`{value:?}`: {message}")]
pub struct InvalidValueError {
    value: Value<'static>,
    message: String,
}

impl InvalidValueError {
    fn new(value: &Value, message: String) -> Self {
        Self {
            value: value.clone().into_owned(),
            message,
        }
    }
}
