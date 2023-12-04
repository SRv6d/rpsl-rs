use crate::rpsl::{
    common::coerce_empty_value,
    error::{InvalidNameError, InvalidValueError},
};
use std::str::FromStr;

/// The name of an attribute.
#[derive(Debug, PartialEq, Eq, Clone)]
pub struct Name(String);

impl FromStr for Name {
    type Err = InvalidNameError;

    /// Create a new `Name` from a string slice.
    ///
    /// A valid name may consist of ASCII letters, digits and the characters "-", "_",
    /// while beginning with a letter and ending with a letter or a digit.
    ///
    /// # Errors
    /// Returns an error if the name is empty or invalid.
    fn from_str(name: &str) -> Result<Self, Self::Err> {
        if name.trim().is_empty() {
            return Err(InvalidNameError::Empty);
        } else if !name.is_ascii() {
            return Err(InvalidNameError::NonAscii);
        } else if !name.chars().next().unwrap().is_ascii_alphabetic() {
            return Err(InvalidNameError::NonAsciiAlphabeticFirstChar);
        } else if !name.chars().last().unwrap().is_ascii_alphanumeric() {
            return Err(InvalidNameError::NonAsciiAlphanumericLastChar);
        }

        Ok(Self(name.to_string()))
    }
}

/// The value of an attribute.
#[derive(Debug, PartialEq, Eq, Clone)]
pub enum Value {
    SingleLine(Option<String>),
    MultiLine(Vec<Option<String>>),
}

impl Value {
    fn validate(value: &str) -> Result<(), InvalidValueError> {
        if !value.is_ascii() {
            return Err(InvalidValueError::NonAscii);
        } else if value.chars().any(|c| c.is_ascii_control()) {
            return Err(InvalidValueError::ContainsControlChar);
        }

        Ok(())
    }
}

impl FromStr for Value {
    type Err = InvalidValueError;

    /// Create a new single line `Value` from a string slice.
    ///
    /// A valid value may consist of any ASCII character, excluding control characters.
    ///
    /// # Errors
    /// Returns an error if the value contains invalid characters.
    fn from_str(value: &str) -> Result<Self, Self::Err> {
        Self::validate(value)?;
        Ok(Self::SingleLine(
            coerce_empty_value(value).map(std::string::ToString::to_string),
        ))
    }
}

impl TryFrom<Vec<&str>> for Value {
    type Error = InvalidValueError;

    /// Create a new `Value` from a vector of string slices.
    ///
    /// A valid value may consist of any ASCII character, excluding control characters.
    ///
    /// # Errors
    /// Returns an error if a value contains invalid characters.
    fn try_from(values: Vec<&str>) -> Result<Self, Self::Error> {
        if values.len() == 1 {
            let value = values[0].parse()?;
            return Ok(value);
        }
        let values = values
            .into_iter()
            .map(|v| {
                Self::validate(v)?;
                Ok(coerce_empty_value(v).map(std::string::ToString::to_string))
            })
            .collect::<Result<Vec<Option<String>>, InvalidValueError>>()?;

        Ok(Self::MultiLine(values))
    }
}

#[derive(Debug, PartialEq, Eq, Clone)]
/// An attribute contained within an RPSL object.
pub struct Attribute {
    /// The name of the attribute.
    pub name: Name,
    /// The value(s) of the attribute.
    pub value: Value,
}

impl Attribute {
    /// Create a new attribute.
    #[must_use]
    pub fn new(name: Name, value: Value) -> Self {
        Self { name, value }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use proptest::prelude::*;

    #[test]
    fn name_from_str() {
        assert_eq!("role".parse::<Name>().unwrap().0, String::from("role"));
        assert_eq!("person".parse::<Name>().unwrap().0, String::from("person"));
    }

    proptest! {
        #[test]
        fn name_from_str_space_only_is_err(n in r"\s") {
            assert!(n.parse::<Name>().is_err());
        }

        #[test]
        fn name_from_str_non_ascii_is_err(n in r"[^[[:ascii:]]]") {
            assert!(n.parse::<Name>().is_err());
        }

        #[test]
        fn name_from_str_non_letter_first_char_is_err(n in r"[^a-zA-Z][[:ascii:]]*") {
            assert!(n.parse::<Name>().is_err());
        }

        #[test]
        fn name_from_str_non_letter_or_digit_last_char_is_err(n in r"[[:ascii:]]*[^a-zA-Z0-9]") {
            assert!(n.parse::<Name>().is_err());
        }
    }

    #[test]
    fn value_from_str() {
        let value = "This is a valid attribute value";
        assert_eq!(
            value.parse::<Value>().unwrap(),
            Value::SingleLine(Some(value.to_string()))
        );
    }

    #[test]
    fn value_from_empty_str() {
        let value = "   ";
        assert_eq!(value.parse::<Value>().unwrap(), Value::SingleLine(None));
    }

    proptest! {
        #[test]
        fn value_from_str_non_ascii_is_err(v in r"[^[[:ascii:]]]") {
            assert!(v.parse::<Name>().is_err());
        }

        #[test]
        fn value_from_str_ascii_control_is_err(v in r"[[:cntrl:]]") {
            assert!(v.parse::<Name>().is_err());
        }
    }

    #[test]
    fn value_from_vec_of_str() {
        assert_eq!(
            Value::try_from(vec!["Packet Street 6", "128 Series of Tubes", "Internet"]).unwrap(),
            Value::MultiLine(vec![
                Some("Packet Street 6".to_string()),
                Some("128 Series of Tubes".to_string()),
                Some("Internet".to_string())
            ])
        );
        assert_eq!(
            Value::try_from(vec!["", "128 Series of Tubes", "Internet"]).unwrap(),
            Value::MultiLine(vec![
                None,
                Some("128 Series of Tubes".to_string()),
                Some("Internet".to_string())
            ])
        );
        assert_eq!(
            Value::try_from(vec!["", " ", "   "]).unwrap(),
            Value::MultiLine(vec![None, None, None])
        );
    }

    #[test]
    fn value_from_vec_w_1_value_is_single_line() {
        assert_eq!(
            Value::try_from(vec!["Packet Street 6"]).unwrap(),
            Value::SingleLine(Some("Packet Street 6".to_string()))
        );
    }
}
