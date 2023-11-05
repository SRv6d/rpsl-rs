use core::panic;

/// The name of an attribute.
#[derive(Debug, PartialEq)]
pub struct Name(String);

impl Name {
    /// Create a new name from a string.
    fn new(name: &str) -> Self {
        if name.trim().is_empty() {
            panic!("Name cannot be empty");
        }
        Self(name.to_string())
    }
}

impl TryFrom<&str> for Name {
    type Error = ();

    fn try_from(name: &str) -> Result<Self, ()> {
        Ok(Self::new(name))
    }
}

/// The value of an attribute.
#[derive(Debug, PartialEq)]
pub enum Value {
    SingleLine(Option<String>),
    MultiLine(Vec<Option<String>>),
}

impl From<&str> for Value {
    /// # Examples
    /// ```
    /// # use rpsl_parser::rpsl;
    /// assert_eq!(
    ///     rpsl::Value::from("ACME Company"),
    ///     rpsl::Value::SingleLine::new(Some("ACME Company".to_string()))
    /// );
    /// assert_eq!(rpsl::Value::from(""), rpsl::Value::SingleLine(None));
    /// assert_eq!(rpsl::Value::from("   "), rpsl::Value::SingleLine(None));
    /// ```
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
    /// # Examples
    /// ```
    /// # use rpsl_parser::rpsl;
    /// assert_eq!(
    ///     rpsl::Value::from(vec![
    ///         "Packet Street 6",
    ///         "128 Series of Tubes",
    ///         "Internet"
    ///     ]),
    ///     rpsl::Value::MultiLine(vec![
    ///         Some("Packet Street 6".to_string()),
    ///         Some("128 Series of Tubes".to_string()),
    ///         Some("Internet".to_string())
    ///     ])
    /// );
    /// assert_eq!(
    ///     rpsl::Value::from(vec!["Packet Street 6"]),
    ///     rpsl::Value::SingleLine(Some("Packet Street 6".to_string())),
    /// );
    /// ```
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
#[derive(Debug, PartialEq)]
/// An attribute contained within an RPSL object.
pub struct Attribute {
    /// The name of the attribute.
    pub name: Name,
    /// The value(s) of the attribute.
    pub value: Value,
}

impl Attribute {
    /// Create a new attribute from an attribute name and it's value(s).
    pub(crate) fn new(name: &str, value: impl Into<Value>) -> Self {
        Self {
            name: name.try_into().unwrap(),
            value: value.into(),
        }
    }
}