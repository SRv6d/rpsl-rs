use std::fmt;
use thiserror::Error;

#[derive(Error, Debug)]
pub enum InvalidNameError {
    #[error("Name cannot be empty")]
    Empty,
}

/// The name of an attribute.
#[derive(Debug, PartialEq, Eq)]
pub struct Name(String);

impl Name {
    /// Create a new name from a string.
    fn new(name: &str) -> Result<Self, InvalidNameError> {
        if name.trim().is_empty() {
            return Err(InvalidNameError::Empty);
        }
        Ok(Self(name.to_string()))
    }
}

impl fmt::Display for Name {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.0)
    }
}

impl TryFrom<&str> for Name {
    type Error = InvalidNameError;

    fn try_from(name: &str) -> Result<Self, InvalidNameError> {
        Self::new(name)
    }
}

impl PartialEq<&str> for Name {
    fn eq(&self, other: &&str) -> bool {
        self.0 == *other
    }
}

/// The value of an attribute.
#[derive(Debug, PartialEq, Eq)]
pub enum Value {
    SingleLine(Option<String>),
    MultiLine(Vec<Option<String>>),
}

impl From<&str> for Value {
    fn from(value: &str) -> Self {
        Self::SingleLine({
            if value.trim().is_empty() {
                None
            } else {
                Some(value.to_string())
            }
        })
    }
}

impl From<Vec<&str>> for Value {
    fn from(values: Vec<&str>) -> Self {
        match values.len() {
            1 => values[0].into(),
            _ => Self::MultiLine(
                values
                    .iter()
                    .map(|v| {
                        if v.trim().is_empty() {
                            return None;
                        }
                        Some((*v).to_string())
                    })
                    .collect(),
            ),
        }
    }
}
#[derive(Debug, PartialEq, Eq)]
/// An attribute contained within an RPSL object.
pub struct Attribute {
    /// The name of the attribute.
    pub name: Name,
    /// The value(s) of the attribute.
    pub value: Value,
}

impl Attribute {
    /// Create a new attribute from an attribute name and it's value(s).
    ///
    /// # Examples
    ///
    /// Create a new `role` attribute with a single value.
    /// ```
    /// # use rpsl_parser::Attribute;
    /// let attribute = Attribute::new("role", "ACME Company");
    /// ```
    ///
    /// Create a new `address` attribute with multiple values describing a complete address.
    /// ```
    /// # use rpsl_parser::Attribute;
    /// let attribute = Attribute::new("address", vec!["Packet Street 6", "128 Series of Tubes", "Internet"]);
    /// ```
    pub fn new(name: &str, value: impl Into<Value>) -> Self {
        Self {
            name: name.try_into().unwrap(),
            value: value.into(),
        }
    }

    /// Create a new attribute without value.
    ///
    /// # Examples
    ///
    /// Create an empty `remarks` attribute.
    /// ```
    /// # use rpsl_parser::Attribute;
    /// let attribute = Attribute::without_value("remarks");
    /// ```
    pub fn without_value(name: &str) -> Self {
        Self {
            name: name.try_into().unwrap(),
            value: Value::SingleLine(None),
        }
    }
}

impl fmt::Display for Attribute {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match &self.value {
            Value::SingleLine(value) => {
                write!(f, "{:16}{}\n", format!("{}:", self.name), {
                    match value {
                        Some(value) => value,
                        None => "",
                    }
                })
            }
            Value::MultiLine(values) => {
                write!(f, "{:16}{}\n", format!("{}:", self.name), {
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
                write!(f, "{}", continuation_values)
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn value_from_str() {
        assert_eq!(
            Value::from("ACME Company"),
            Value::SingleLine(Some("ACME Company".to_string()))
        );
        assert_eq!(Value::from(""), Value::SingleLine(None));
        assert_eq!(Value::from("   "), Value::SingleLine(None));
    }

    #[test]
    fn value_from_vec_of_str() {
        assert_eq!(
            Value::from(vec!["Packet Street 6", "128 Series of Tubes", "Internet"]),
            Value::MultiLine(vec![
                Some("Packet Street 6".to_string()),
                Some("128 Series of Tubes".to_string()),
                Some("Internet".to_string())
            ])
        );
        assert_eq!(
            Value::from(vec!["Packet Street 6"]),
            Value::SingleLine(Some("Packet Street 6".to_string())),
        );
        assert_eq!(
            Value::from(vec!["", "128 Series of Tubes", "Internet"]),
            Value::MultiLine(vec![
                None,
                Some("128 Series of Tubes".to_string()),
                Some("Internet".to_string())
            ])
        );
        assert_eq!(
            Value::from(vec!["", " ", "   "]),
            Value::MultiLine(vec![None, None, None])
        );
    }

    #[test]
    fn attribute_display_single_line() {
        assert_eq!(
            Attribute::new("ASNumber", "32934").to_string(),
            "ASNumber:       32934\n"
        );
        assert_eq!(
            Attribute::new("ASName", "FACEBOOK").to_string(),
            "ASName:         FACEBOOK\n"
        );
        assert_eq!(
            Attribute::new("RegDate", "2004-08-24").to_string(),
            "RegDate:        2004-08-24\n"
        );
        assert_eq!(
            Attribute::new("Ref", "https://rdap.arin.net/registry/autnum/32934").to_string(),
            "Ref:            https://rdap.arin.net/registry/autnum/32934\n"
        );
    }

    #[test]
    fn attribute_display_multi_line() {
        assert_eq!(
            Attribute::new(
                "remarks",
                vec![
                    "AS1299 is matching RPKI validation state and reject",
                    "invalid prefixes from peers and customers."
                ]
            )
            .to_string(),
            concat!(
                "remarks:        AS1299 is matching RPKI validation state and reject\n",
                "                invalid prefixes from peers and customers.\n",
            )
        );
    }
}
