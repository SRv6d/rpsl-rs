use super::{attribute::Attribute, error::AttributeError};
use std::fmt::Debug;

pub trait Specification: Debug + Clone + Copy {
    fn validate_attribute(attribute: &Attribute) -> Result<(), AttributeError>;
}

#[derive(Debug, Default, Clone, Copy, PartialEq, Eq)]
pub struct Raw;

impl Specification for Raw {
    fn validate_attribute(_attribute: &Attribute) -> Result<(), AttributeError> {
        Ok(())
    }
}

#[derive(Debug, Default, Clone, Copy, PartialEq, Eq)]
pub struct Rfc2622;

impl Specification for Rfc2622 {
    fn validate_attribute(_attribute: &Attribute) -> Result<(), AttributeError> {
        todo!()
    }
}
