//! Specifications and validation rules for RPSL objects.
//!
//! This module defines specifications that values can optionally be validated into after parsing.

use super::attribute::{Attribute, Name, Value};
use std::fmt::Debug;

/// Defines how parsed attributes should be validated for a given specification.
pub trait Specification: Debug + Clone + Copy {
    /// Validate a single attribute according to the specification.
    ///
    /// # Errors
    /// Returns an [`AttributeError`] when the attribute name or value does not satisfy
    /// the specification's rules.
    fn validate_attribute(attribute: &Attribute<'_, Self>) -> Result<(), AttributeError<Self>>;
}

/// Default specification after parsing, does not perform any validation.
#[derive(Debug, Default, Clone, Copy, PartialEq, Eq)]
pub struct Raw;

impl Specification for Raw {
    fn validate_attribute(_attribute: &Attribute<'_, Self>) -> Result<(), AttributeError<Self>> {
        Ok(())
    }
}

/// Validation rules matching RFC 2622.
#[derive(Debug, Default, Clone, Copy, PartialEq, Eq)]
pub struct Rfc2622;

impl Rfc2622 {
    fn validate_name<S: Specification>(name: &Name<S>) -> Result<(), InvalidNameError<S>> {
        if name.len() < 2 {
            return Err(InvalidNameError::new(
                name,
                "must be at least two characters long",
            ));
        }

        if !name.is_ascii() {
            return Err(InvalidNameError::new(
                name,
                "must contain only ASCII characters",
            ));
        }

        let mut chars = name.chars();
        let first = chars.next().expect("must have a first character");
        let last = name.chars().last().expect("must have a last character");
        if !first.is_ascii_alphabetic() {
            return Err(InvalidNameError::new(
                name,
                "must start with an ASCII alphabetic character",
            ));
        }
        if !last.is_ascii_alphanumeric() {
            return Err(InvalidNameError::new(
                name,
                "must end with an ASCII alphanumeric character",
            ));
        }

        if !name
            .chars()
            .all(|c| c.is_ascii_alphanumeric() || c == '-' || c == '_')
        {
            return Err(InvalidNameError::new(
                name,
                "may only contain ASCII letters, digits, '-' or '_'",
            ));
        }

        Ok(())
    }

    fn validate_value<S: Specification>(value: &Value<S>) -> Result<(), InvalidValueError<S>> {
        let validator = |v: &str| {
            if !v.is_ascii() {
                return Err(InvalidValueError::new(
                    value,
                    "must contain only ASCII characters",
                ));
            }

            if v.chars().any(|c| c.is_ascii_control()) {
                return Err(InvalidValueError::new(
                    value,
                    "must not contain ASCII control characters",
                ));
            }

            if v.starts_with(|c: char| c.is_ascii_whitespace()) {
                return Err(InvalidValueError::new(
                    value,
                    "must not start with whitespace",
                ));
            }

            Ok(())
        };
        for v in value.with_content() {
            validator(v)?;
        }

        Ok(())
    }
}

impl Specification for Rfc2622 {
    fn validate_attribute(attribute: &Attribute<'_, Self>) -> Result<(), AttributeError<Self>> {
        Self::validate_name(&attribute.name)?;
        Self::validate_value(&attribute.value)?;
        Ok(())
    }
}

#[derive(thiserror::Error, Debug)]
/// An invalid attribute was encountered during validation.
pub enum AttributeError<S: Specification = Raw> {
    /// The name of the attribute is invalid.
    #[error("invalid attribute name {0}")]
    InvalidName(#[from] InvalidNameError<S>),
    /// The value of the attribute is invalid.
    #[error("invalid attribute value {0}")]
    InvalidValue(#[from] InvalidValueError<S>),
}

/// The attribute has an invalid name.
#[derive(thiserror::Error, Debug)]
#[error("`{name}`: {message}")]
pub struct InvalidNameError<S: Specification> {
    name: Name<'static, S>,
    message: String,
}

impl<S: Specification> InvalidNameError<S> {
    fn new(name: &Name<S>, message: impl Into<String>) -> Self {
        Self {
            name: name.clone().into_owned(),
            message: message.into(),
        }
    }
}

/// The attribute has an invalid value.
#[derive(thiserror::Error, Debug)]
#[error("`{value:?}`: {message}")]
pub struct InvalidValueError<S: Specification> {
    value: Value<'static, S>,
    message: String,
}

impl<S: Specification> InvalidValueError<S> {
    fn new(value: &Value<S>, message: impl Into<String>) -> Self {
        Self {
            value: value.clone().into_owned(),
            message: message.into(),
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
        fn rfc2622_attribute_value_non_ascii_is_err(
            value in r"[^[:ascii:]]"
                .prop_filter("value should not be empty", |value| !value.trim().is_empty())
        ) {
            let v = Value::new_single(value);
            assert!(Rfc2622::validate_value(&v).is_err());
        }
    }

    proptest! {
        #[test]
        fn rfc2622_attribute_value_ascii_control_is_err(
            value in r"[[:cntrl:]]"
                .prop_filter("value should not be empty", |value| !value.trim().is_empty())
        ) {
            let v = Value::new_single(value);
            assert!(Rfc2622::validate_value(&v).is_err());
        }
    }
}
