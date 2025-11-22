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

impl Rfc2622 {
    fn validate_name<S: Specification>(name: &Name<'_, S>) -> Result<(), InvalidNameError> {
        todo!()
    }

    fn validate_value<S: Specification>(value: &Value<'_, S>) -> Result<(), InvalidValueError> {
        todo!()
    }
}

impl Specification for Rfc2622 {
    fn validate_attribute<S: Specification>(
        attribute: &Attribute<'_, S>,
    ) -> Result<(), AttributeError> {
        Self::validate_name(&attribute.name)?;
        Self::validate_value(&attribute.value)?;
        Ok(())
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

#[cfg(test)]
mod tests {

    use proptest::prelude::*;
    use rstest::*;

    use crate::{spec::Rfc2622, Attribute, Name, Value};

    #[rstest]
    #[case("aut-num", "AS3257")]
    #[case("ASNumber", "32934")]
    #[case("phone", "+49 176 07071964")]
    #[case("address", "* Equinix FR5, Kleyerstr, Frankfurt am Main")]
    #[case("remarks", "Concerning abuse and spam ... mailto: abuse@asn.net")]
    fn rfc2622_valid_attribute(#[case] name: &str, #[case] value: &str) {
        let attribute = Attribute::new(name, value);
        attribute.validate::<Rfc2622>().unwrap();
    }

    #[test]
    fn rfc2622_attribute_name_single_letter_is_error() {
        let n = Name::new("a");
        assert!(Rfc2622::validate_name(&n).is_err());
    }

    proptest! {
        #[test]
        fn rfc2622_attribute_name_non_letter_first_char_is_error(char in r"[^A-Za-z]") {
            let n = Name::new(format!("{char}remarks"));
            assert!(Rfc2622::validate_name(&n).is_err());
        }
    }

    proptest! {
        #[test]
        fn rfc2622_attribute_name_non_letter_or_digit_last_char_is_error(char in r"[^A-Za-z0-9]") {
            let n = Name::new(format!("remarks{char}"));
            assert!(Rfc2622::validate_name(&n).is_err());
        }
    }

    proptest! {
        #[test]
        fn rfc2622_attribute_name_space_only_is_error(name in r"\s") {
            let n = Name::new(name);
            assert!(Rfc2622::validate_name(&n).is_err());
        }
    }

    proptest! {
        #[test]
        fn rfc2622_attribute_name_non_ascii_is_err(name in r"[^[:ascii:]]") {
            let n = Name::new(name);
            assert!(Rfc2622::validate_name(&n).is_err());
        }
    }

    proptest! {
        #[test]
        fn rfc2622_attribute_value_non_ascii_is_err(value in r"[^[:ascii:]]") {
            let v = Value::new_single(value);
            assert!(Rfc2622::validate_value(&v).is_err());
        }
    }

    proptest! {
        #[test]
        fn rfc2622_attribute_value_ascii_control_is_err(value in r"[[:cntrl:]]") {
            let v = Value::new_single(value);
            assert!(Rfc2622::validate_value(&v).is_err());
        }
    }
}
