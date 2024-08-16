use crate::{
    common::coerce_empty_value,
    error::{InvalidNameError, InvalidValueError},
};
use std::{borrow::Cow, fmt, ops::Deref, str::FromStr};

/// An attribute of an [`Object`](crate::Object).
#[derive(Debug, PartialEq, Eq, Clone)]
pub struct Attribute<'a> {
    /// The name of the attribute.
    pub name: Name<'a>,
    /// The value(s) of the attribute.
    pub value: Value<'a>,
}

impl<'a> Attribute<'a> {
    /// Create a new attribute.
    #[must_use]
    pub fn new(name: Name<'a>, value: Value<'a>) -> Self {
        Self { name, value }
    }
}

impl fmt::Display for Attribute<'_> {
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

/// The name of an attribute.
#[derive(Debug, PartialEq, Eq, Clone)]
pub struct Name<'a>(Cow<'a, str>);

impl FromStr for Name<'_> {
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

        Ok(Self(Cow::Owned(name.to_string())))
    }
}

impl Deref for Name<'_> {
    type Target = str;

    fn deref(&self) -> &Self::Target {
        self.0.as_ref()
    }
}

impl PartialEq<&str> for Name<'_> {
    fn eq(&self, other: &&str) -> bool {
        self.0 == *other
    }
}

impl fmt::Display for Name<'_> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.0)
    }
}

/// The value of an attribute.
#[derive(Debug, PartialEq, Eq, Clone)]
pub enum Value<'a> {
    SingleLine(Option<Cow<'a, str>>),
    MultiLine(Vec<Option<Cow<'a, str>>>),
}

impl<'a> Value<'a> {
    fn validate(value: &str) -> Result<(), InvalidValueError> {
        if !value.is_ascii() {
            return Err(InvalidValueError::NonAscii);
        } else if value.chars().any(|c| c.is_ascii_control()) {
            return Err(InvalidValueError::ContainsControlChar);
        }

        Ok(())
    }

    /// The number of individual values contained.
    pub fn len(&self) -> usize {
        match &self {
            Self::SingleLine(_) => 1,
            Self::MultiLine(values) => values.len(),
        }
    }

    /// The values referenced within the view that do not contain empty values.
    ///
    /// # Example
    /// ```
    /// # use rpsl::parse_object;
    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
    /// let remarks = parse_object("
    /// remarks:        I have lots
    ///                 
    ///                 to say.
    ///
    /// ")?;
    /// assert_eq!(remarks[0].value.with_content(), vec!["I have lots", "to say."]);
    /// # Ok(())
    /// # }
    /// ```
    pub fn with_content(&self) -> Vec<&str> {
        match self {
            Self::SingleLine(v) => {
                if let Some(v) = v {
                    vec![v]
                } else {
                    vec![]
                }
            }
            Self::MultiLine(v) => todo!(),
        }
    }
}

impl FromStr for Value<'_> {
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
            coerce_empty_value(value).map(|value| Cow::Owned(value.to_string())),
        ))
    }
}

impl TryFrom<Vec<&str>> for Value<'_> {
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

        Ok(Self::MultiLine(
            values.into_iter().map(|v| v.map(Cow::Owned)).collect(),
        ))
    }
}

impl IntoIterator for Value<'_> {
    type Item = Option<String>;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        todo!()
    }
}

impl PartialEq<&str> for Value<'_> {
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

impl PartialEq<Vec<&str>> for Value<'_> {
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

impl PartialEq<Vec<Option<&str>>> for Value<'_> {
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
