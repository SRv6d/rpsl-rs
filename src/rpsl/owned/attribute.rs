use crate::rpsl::{
    common::coerce_empty_value,
    error::{InvalidNameError, InvalidValueError},
};
use std::{fmt, str::FromStr};

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

impl PartialEq<&str> for Name {
    fn eq(&self, other: &&str) -> bool {
        self.0 == *other
    }
}

impl fmt::Display for Name {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.0)
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

    /// The number of values contained within.
    pub fn len(&self) -> usize {
        match &self {
            Value::SingleLine(_) => 1,
            Value::MultiLine(values) => values.len(),
        }
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

impl IntoIterator for Value {
    type Item = Option<String>;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        match self {
            Self::SingleLine(value) => vec![value].into_iter(),
            Self::MultiLine(values) => values.into_iter(),
        }
    }
}

impl PartialEq<&str> for Value {
    fn eq(&self, other: &&str) -> bool {
        match &self {
            Self::MultiLine(_) => false,
            Self::SingleLine(value) => match value {
                Some(value) => value == *other,
                None => coerce_empty_value(other).is_none(),
            },
        }
    }
}

impl PartialEq<Vec<&str>> for Value {
    fn eq(&self, other: &Vec<&str>) -> bool {
        match &self {
            Self::SingleLine(_) => false,
            Self::MultiLine(values) => {
                if values.len() != other.len() {
                    return false;
                }

                let other_coerced = other.iter().map(|&v| coerce_empty_value(v));

                for (s, o) in values.iter().zip(other_coerced) {
                    if s.as_deref() != o {
                        return false;
                    }
                }

                true
            }
        }
    }
}

impl PartialEq<Vec<Option<&str>>> for Value {
    fn eq(&self, other: &Vec<Option<&str>>) -> bool {
        match &self {
            Self::SingleLine(_) => false,
            Self::MultiLine(values) => {
                if values.len() != other.len() {
                    return false;
                }

                for (s, o) in values.iter().zip(other.iter()) {
                    if s.as_deref() != *o {
                        return false;
                    }
                }

                true
            }
        }
    }
}

#[derive(Debug, PartialEq, Eq, Clone)]
/// An attribute of an RPSL [`Object`](crate::Object).
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

impl fmt::Display for Attribute {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match &self.value {
            Value::SingleLine(value) => {
                writeln!(f, "{:16}{}", format!("{}:", self.name), {
                    match value {
                        Some(value) => value,
                        None => "",
                    }
                })
            }
            Value::MultiLine(values) => {
                writeln!(f, "{:16}{}", format!("{}:", self.name), {
                    match &values[0] {
                        Some(value) => value,
                        None => "",
                    }
                })?;

                let mut continuation_values = String::new();
                for value in &values[1..] {
                    continuation_values.push_str(&format!("{:16}{}\n", "", {
                        match &value {
                            Some(value) => value,
                            None => "",
                        }
                    }));
                }
                write!(f, "{continuation_values}")
            }
        }
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

    #[test]
    fn value_len() {
        assert_eq!("single value".parse::<Value>().unwrap().len(), 1);
        assert_eq!(
            std::convert::TryInto::<Value>::try_into(vec!["multi", "value", "attribute"])
                .unwrap()
                .len(),
            3
        );
    }

    #[test]
    fn value_eq_is_eq() {
        assert_eq!(
            Value::SingleLine(Some("single value".to_string())),
            "single value"
        );
        assert_eq!(Value::SingleLine(None), " ");
        assert_eq!(
            Value::MultiLine(vec![
                Some("multi".to_string()),
                Some("value".to_string()),
                Some("attribute".to_string())
            ]),
            vec!["multi", "value", "attribute"]
        );
        assert_eq!(
            Value::MultiLine(vec![
                Some("multi".to_string()),
                None,
                Some("attribute".to_string())
            ]),
            vec!["multi", "    ", "attribute"]
        );
        assert_eq!(
            Value::MultiLine(vec![
                Some("multi".to_string()),
                Some("value".to_string()),
                Some("attribute".to_string())
            ]),
            vec![Some("multi"), Some("value"), Some("attribute")]
        );
        assert_eq!(
            Value::MultiLine(vec![
                Some("multi".to_string()),
                None,
                Some("attribute".to_string())
            ]),
            vec![Some("multi"), None, Some("attribute")]
        );
    }

    #[test]
    fn value_ne_is_ne() {
        assert_ne!(
            Value::SingleLine(Some("single value".to_string())),
            "other single value"
        );
        assert_ne!(Value::SingleLine(None), "not none");
        assert_ne!(
            Value::SingleLine(Some("single value".to_string())),
            vec!["other", "multi", "value", "attribute"]
        );
        assert_ne!(
            Value::MultiLine(vec![
                Some("multi".to_string()),
                Some("value".to_string()),
                Some("attribute".to_string())
            ]),
            vec!["other", "multi", "value", "attribute"]
        );
        assert_ne!(
            Value::MultiLine(vec![
                Some("multi".to_string()),
                Some("value".to_string()),
                Some("attribute".to_string())
            ]),
            vec![Some("multi"), None, Some("attribute")]
        );
        assert_ne!(
            Value::MultiLine(vec![
                Some("multi".to_string()),
                None,
                Some("attribute".to_string())
            ]),
            vec![Some("multi"), Some("    "), Some("attribute")]
        );
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

    #[test]
    fn attribute_display_single_line() {
        assert_eq!(
            Attribute::new("ASNumber".parse().unwrap(), "32934".parse().unwrap()).to_string(),
            "ASNumber:       32934\n"
        );
        assert_eq!(
            Attribute::new("ASName".parse().unwrap(), "FACEBOOK".parse().unwrap()).to_string(),
            "ASName:         FACEBOOK\n"
        );
        assert_eq!(
            Attribute::new("RegDate".parse().unwrap(), "2004-08-24".parse().unwrap()).to_string(),
            "RegDate:        2004-08-24\n"
        );
        assert_eq!(
            Attribute::new(
                "Ref".parse().unwrap(),
                "https://rdap.arin.net/registry/autnum/32934"
                    .parse()
                    .unwrap()
            )
            .to_string(),
            "Ref:            https://rdap.arin.net/registry/autnum/32934\n"
        );
    }

    #[test]
    fn attribute_display_multi_line() {
        assert_eq!(
            Attribute::new(
                "remarks".parse().unwrap(),
                vec![
                    "AS1299 is matching RPKI validation state and reject",
                    "invalid prefixes from peers and customers."
                ]
                .try_into()
                .unwrap()
            )
            .to_string(),
            concat!(
                "remarks:        AS1299 is matching RPKI validation state and reject\n",
                "                invalid prefixes from peers and customers.\n",
            )
        );
    }
}
