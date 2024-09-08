use std::{borrow::Cow, fmt, ops::Deref, str::FromStr};

use crate::error::{InvalidNameError, InvalidValueError};

use serde::Serialize;

/// An attribute of an [`Object`](crate::Object).
///
/// # Example
/// ```
/// # use rpsl::{parse_object, Attribute};
/// let object = parse_object("
/// name:           ACME Company
///
/// ")?;
/// let attribute = Attribute::new("name".parse()?, "ACME Company".parse()?);
/// assert_eq!(object[0], attribute);
/// # Ok::<(), Box<dyn std::error::Error>>(())
/// ```
#[derive(Debug, PartialEq, Eq, Clone)]
pub struct Attribute<'a> {
    /// The name of the attribute.
    pub name: Name<'a>,
    /// The value of the attribute.
    pub value: Value<'a>,
}

impl<'a> Attribute<'a> {
    /// Create a new attribute.
    #[must_use]
    pub fn new(name: Name<'a>, value: Value<'a>) -> Self {
        Self { name, value }
    }

    pub(crate) fn unchecked_single<V>(name: &'a str, value: V) -> Self
    where
        V: Into<Option<&'a str>>,
    {
        let name = Name::unchecked(name);
        let value = Value::unchecked_single(value);
        Self { name, value }
    }

    pub(crate) fn unchecked_multi<I, V>(name: &'a str, values: I) -> Self
    where
        I: IntoIterator<Item = V>,
        V: Into<Option<&'a str>>,
    {
        let name = Name::unchecked(name);
        let value = Value::unchecked_multi(values);
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

/// The name of an [`Attribute`].
#[derive(Debug, PartialEq, Eq, Clone, Serialize)]
#[serde(transparent)]
pub struct Name<'a>(Cow<'a, str>);

impl<'a> Name<'a> {
    fn unchecked(name: &'a str) -> Self {
        Self(Cow::Borrowed(name))
    }
}

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

/// The value of an [`Attribute`].
/// Since only some values contain multiple lines and single line values do not require
/// additional heap allocation, an Enum is used to represent both variants.
#[derive(Debug, PartialEq, Eq, Clone)]
pub enum Value<'a> {
    /// A single line value.
    ///
    /// # Example
    /// ```
    /// # use rpsl::{parse_object, Value};
    /// let object = parse_object("
    /// name:           ACME Company
    ///
    /// ")?;
    /// let value: Value = "ACME Company".parse()?;
    /// assert_eq!(object[0].value, value);
    /// # Ok::<(), Box<dyn std::error::Error>>(())
    /// ```
    SingleLine(Option<Cow<'a, str>>),
    /// A value spanning over multiple lines.
    ///
    /// # Example
    /// ```
    /// # use rpsl::{parse_object, Value};
    /// let object = parse_object("
    /// remarks:        Packet Street 6
    ///                 128 Series of Tubes
    ///                 Internet
    ///
    /// ")?;
    /// let value: Value = vec!["Packet Street 6", "128 Series of Tubes", "Internet"].try_into()?;
    /// assert_eq!(object[0].value, value);
    /// # Ok::<(), Box<dyn std::error::Error>>(())
    /// ```
    MultiLine(Vec<Option<Cow<'a, str>>>),
}

impl<'a> Value<'a> {
    /// Create a single line value without checking that characters conform to any specification
    /// while still coercing empty values to `None`.
    fn unchecked_single<V>(value: V) -> Self
    where
        V: Into<Option<&'a str>>,
    {
        Self::SingleLine(value.into().and_then(coerce_empty_value).map(Cow::Borrowed))
    }

    /// Create a multi line value without checking that characters conform to any specification
    /// while still coercing empty values to `None`.
    fn unchecked_multi<I, V>(values: I) -> Self
    where
        I: IntoIterator<Item = V>,
        V: Into<Option<&'a str>>,
    {
        let s = Self::MultiLine(
            values
                .into_iter()
                .map(|v| v.into().and_then(coerce_empty_value).map(Cow::Borrowed))
                .collect(),
        );
        assert!(s.lines() > 1, "multi line values need at least two lines");
        s
    }

    fn validate(value: &str) -> Result<(), InvalidValueError> {
        if !value.is_ascii() {
            return Err(InvalidValueError::NonAscii);
        } else if value.chars().any(|c| c.is_ascii_control()) {
            return Err(InvalidValueError::ContainsControlChar);
        }

        Ok(())
    }

    /// The number of lines contained.
    ///
    /// # Examples
    ///
    /// A value with a single line.
    /// ```
    /// # use rpsl::Value;
    /// let value: Value = "ACME Company".parse()?;
    /// assert_eq!(value.lines(), 1);
    /// # Ok::<(), Box<dyn std::error::Error>>(())
    /// ```
    ///
    /// A value with multiple lines.
    /// ```
    /// # use rpsl::Value;
    /// let value: Value = vec!["Packet Street 6", "128 Series of Tubes", "Internet"].try_into()?;
    /// assert_eq!(value.lines(), 3);
    /// # Ok::<(), Box<dyn std::error::Error>>(())
    /// ```
    #[must_use]
    pub fn lines(&self) -> usize {
        match &self {
            Self::SingleLine(_) => 1,
            Self::MultiLine(values) => values.len(),
        }
    }

    /// The lines that contain content and are non empty.
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
            Self::MultiLine(v) => v.iter().flatten().map(AsRef::as_ref).collect(),
        }
    }
}

impl FromStr for Value<'_> {
    type Err = InvalidValueError;

    /// Create a new single line value from a string slice.
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

    /// Create a new value from a vector of string slices, representing the values lines.
    ///
    /// # Errors
    /// Returns an error if a value contains invalid characters.
    ///
    /// # Example
    /// ```
    /// # use rpsl::Value;
    /// let value: Value = vec!["Packet Street 6", "128 Series of Tubes", "Internet"].try_into()?;
    /// assert_eq!(value.lines(), 3);
    /// # Ok::<(), Box<dyn std::error::Error>>(())
    /// ```
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

#[allow(clippy::from_over_into)]
impl Into<Vec<Option<String>>> for Value<'_> {
    fn into(self) -> Vec<Option<String>> {
        match self {
            Self::SingleLine(value) => {
                vec![value.map(|v| v.to_string())]
            }
            Self::MultiLine(values) => values
                .into_iter()
                .map(|v| v.map(|v| v.to_string()))
                .collect(),
        }
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
        if self.lines() != other.len() {
            return false;
        }

        match &self {
            Self::SingleLine(value) => {
                let s = value.as_deref();
                let other_coerced = coerce_empty_value(other[0]);
                s == other_coerced
            }
            Self::MultiLine(values) => {
                let s = values.iter().map(|v| v.as_deref());
                let other_coerced = other.iter().map(|&v| coerce_empty_value(v));
                s.eq(other_coerced)
            }
        }
    }
}

impl PartialEq<Vec<Option<&str>>> for Value<'_> {
    fn eq(&self, other: &Vec<Option<&str>>) -> bool {
        if self.lines() != other.len() {
            return false;
        }

        match &self {
            Self::SingleLine(value) => {
                let s = value.as_deref();
                let other = other[0];
                s == other
            }
            Self::MultiLine(values) => {
                let s = values.iter().map(|v| v.as_deref());
                let other = other.iter().map(|v| v.as_deref());
                s.eq(other)
            }
        }
    }
}

/// Coerce an empty value to `None`.
fn coerce_empty_value<S>(value: S) -> Option<S>
where
    S: AsRef<str>,
{
    if value.as_ref().trim().is_empty() {
        None
    } else {
        Some(value)
    }
}

#[cfg(test)]
mod tests {
    use proptest::prelude::*;
    use rstest::*;
    use serde_test::{assert_ser_tokens, Token};

    use super::*;

    #[rstest]
    #[case(
        Attribute::new("ASNumber".parse().unwrap(), "32934".parse().unwrap()),
        "ASNumber:       32934\n"
    )]
    #[case(
        Attribute::new("ASName".parse().unwrap(), "FACEBOOK".parse().unwrap()),
        "ASName:         FACEBOOK\n"
    )]
    #[case(
        Attribute::new("RegDate".parse().unwrap(), "2004-08-24".parse().unwrap()),
        "RegDate:        2004-08-24\n"
    )]
    #[case(
        Attribute::new(
            "Ref".parse().unwrap(),
            "https://rdap.arin.net/registry/autnum/32934".parse().unwrap()
        ),
        "Ref:            https://rdap.arin.net/registry/autnum/32934\n"
    )]
    fn attribute_display_single_line(#[case] attribute: Attribute, #[case] expected: &str) {
        assert_eq!(attribute.to_string(), expected);
    }

    #[rstest]
    #[case(
        Attribute::new(
            "remarks".parse().unwrap(),
            vec![
                "AS1299 is matching RPKI validation state and reject",
                "invalid prefixes from peers and customers."
            ]
            .try_into()
            .unwrap()
        ),
        concat!(
            "remarks:        AS1299 is matching RPKI validation state and reject\n",
            "                invalid prefixes from peers and customers.\n",
        )
    )]
    fn attribute_display_multi_line(#[case] attribute: Attribute, #[case] expected: &str) {
        assert_eq!(attribute.to_string(), expected);
    }

    #[rstest]
    #[case(
        Attribute::new(Name::unchecked("ASNumber"), Value::unchecked_single("32934")),
        &[
            Token::Struct { name: "Attribute", len: 2 },
            Token::Str("name"),
            Token::Str("ASNumber"),
            Token::Str("values"),
            Token::Seq { len: Some(1) },
            Token::Str("32934"),
            Token::SeqEnd,
            Token::StructEnd,
        ],
    )]
    #[case(
        Attribute::new(
            Name::unchecked("address"),
            Value::unchecked_multi(["Packet Street 6", "128 Series of Tubes", "Internet"])
        ),
        &[
            Token::Struct { name: "Attribute", len: 2 },
            Token::Str("name"),
            Token::Str("address"),
            Token::Str("values"),
            Token::Seq { len: Some(3) },
            Token::Str("Packet Street 6"),
            Token::Str("128 Series of Tubes"),
            Token::Str("Internet"),
            Token::SeqEnd,
            Token::StructEnd,
        ],
    )]
    fn attribute_serialize(#[case] attribute: Attribute, #[case] expected: &[Token]) {
        assert_ser_tokens(&attribute, expected);
    }

    #[test]
    fn name_display() {
        let name_display = Name::from_str("address").unwrap().to_string();
        assert_eq!(name_display, "address");
    }

    #[rstest]
    #[case("role")]
    #[case("person")]
    fn name_from_str(#[case] s: &str) {
        assert_eq!(Name::from_str(s).unwrap(), Name(Cow::Owned(s.to_string())));
    }

    proptest! {
        #[test]
        fn name_from_str_space_only_is_err(n in r"\s") {
            assert!(Name::from_str(&n).is_err());
        }

        #[test]
        fn name_from_str_non_ascii_is_err(n in r"[^[[:ascii:]]]") {
            assert!(Name::from_str(&n).is_err());
        }

        #[test]
        fn name_from_str_non_letter_first_char_is_err(n in r"[^a-zA-Z][[:ascii:]]*") {
            assert!(Name::from_str(&n).is_err());
        }

        #[test]
        fn name_from_str_non_letter_or_digit_last_char_is_err(n in r"[[:ascii:]]*[^a-zA-Z0-9]") {
            assert!(Name::from_str(&n).is_err());
        }
    }

    #[rstest]
    #[case(Name::unchecked("ASNumber"), Token::Str("ASNumber"))]
    fn name_serialize(#[case] name: Name, #[case] expected: Token) {
        assert_ser_tokens(&name, &[expected]);
    }

    #[rstest]
    #[case("This is a valid attribute value", Value::SingleLine(Some(Cow::Owned("This is a valid attribute value".to_string()))))]
    #[case("   ", Value::SingleLine(None))]
    fn value_from_str(#[case] s: &str, #[case] expected: Value) {
        assert_eq!(Value::from_str(s).unwrap(), expected);
    }

    #[rstest]
    fn value_from_empty_str(#[values("", "   ")] s: &str) {
        assert_eq!(Value::from_str(s).unwrap(), Value::SingleLine(None));
    }

    #[rstest]
    #[case(
        Value::unchecked_single("32934"),
        &[
            Token::Seq { len: Some(1) },
            Token::Str("32934"),
            Token::SeqEnd,
        ],
    )]
    #[case(
        Value::unchecked_single(""),
        &[
            Token::Seq { len: Some(1) },
            Token::None,
            Token::SeqEnd,
        ],
    )]
    #[case(
        Value::unchecked_multi(["Packet Street 6", "128 Series of Tubes", "Internet"]),
        &[
            Token::Seq { len: Some(3) },
            Token::Str("Packet Street 6"),
            Token::Str("128 Series of Tubes"),
            Token::Str("Internet"),
            Token::SeqEnd,
        ],
    )]
    fn value_serialize(#[case] value: Value, #[case] expected: &[Token]) {
        assert_ser_tokens(&value, expected);
    }

    #[rstest]
    #[case(Value::unchecked_single(""), Value::unchecked_single(None))]
    #[case(Value::unchecked_single("   "), Value::unchecked_single(None))]
    #[case(Value::unchecked_multi(["", " ", "   "]), Value::unchecked_multi([None, None, None]))]
    /// Creating unchecked values from empty strings results in None values.
    fn value_unchecked_empty_is_none(#[case] value: Value, #[case] expected: Value) {
        assert_eq!(value, expected);
    }

    #[test]
    #[should_panic(expected = "multi line values need at least two lines")]
    /// Unchecked multi line attributes cannot be created with only a single value.
    fn value_unchecked_multi_with_singe_value_panics() {
        Value::unchecked_multi(["just one"]);
    }

    #[rstest]
    #[case(
        vec!["Packet Street 6", "128 Series of Tubes", "Internet"],
        Value::MultiLine(vec![
            Some(Cow::Owned("Packet Street 6".to_string())),
            Some(Cow::Owned("128 Series of Tubes".to_string())),
            Some(Cow::Owned("Internet".to_string()))
        ])
    )]
    #[case(
        vec!["", "128 Series of Tubes", "Internet"],
        Value::MultiLine(vec![
            None,
            Some(Cow::Owned("128 Series of Tubes".to_string())),
            Some(Cow::Owned("Internet".to_string()))
        ])
    )]
    #[case(
        vec!["", " ", "   "],
        Value::MultiLine(vec![None, None, None])
    )]
    fn value_from_vec_of_str(#[case] v: Vec<&str>, #[case] expected: Value) {
        let value = Value::try_from(v).unwrap();
        assert_eq!(value, expected);
    }

    #[test]
    fn value_from_vec_w_1_value_is_single_line() {
        assert_eq!(
            Value::try_from(vec!["Packet Street 6"]).unwrap(),
            Value::SingleLine(Some(Cow::Owned("Packet Street 6".to_string())))
        );
    }

    #[rstest]
    #[case("single value", 1)]
    #[case(vec!["multi", "value", "attribute"].try_into().unwrap(), 3)]
    fn value_lines(#[case] value: Value, #[case] expected: usize) {
        assert_eq!(value.lines(), expected);
    }

    #[rstest]
    #[case(
        Value::SingleLine(None),
        vec![]
    )]
    #[case(
        Value::SingleLine(Some(Cow::Owned("single value".to_string()))),
        vec!["single value"]
    )]
    #[case(
        Value::MultiLine(vec![
            None,
            Some(Cow::Owned("128 Series of Tubes".to_string())),
            Some(Cow::Owned("Internet".to_string()))
        ]),
        vec!["128 Series of Tubes", "Internet"]
    )]
    #[case(
        Value::MultiLine(vec![
            Some(Cow::Owned("Packet Street 6".to_string())),
            Some(Cow::Owned("128 Series of Tubes".to_string())),
            Some(Cow::Owned("Internet".to_string()))
        ]),
        vec!["Packet Street 6", "128 Series of Tubes", "Internet"]
    )]
    fn value_with_content(#[case] value: Value, #[case] expected: Vec<&str>) {
        let content = value.with_content();
        assert_eq!(content, expected);
    }

    #[rstest]
    #[case("a value")]
    #[case("single value")]
    /// A value and &str evaluate as equal if the contents match.
    fn value_partialeq_str_eq_is_eq(#[case] s: &str) {
        let value = Value::SingleLine(Some(Cow::Owned(s.to_string())));
        assert_eq!(value, s);
    }

    #[rstest]
    #[case(
        Value::SingleLine(Some(Cow::Owned("a value".to_string()))),
        "a different value"
    )]
    #[case(
        Value::MultiLine(vec![
            Some(Cow::Owned("multi".to_string())),
            Some(Cow::Owned("value".to_string()))
        ]),
       "single value"
    )]
    /// A value and &str do not evaluate as equal if the contents differ.
    fn value_partialeq_str_ne_is_ne(#[case] value: Value, #[case] s: &str) {
        assert_ne!(value, s);
    }

    #[rstest]
    #[case(
        Value::SingleLine(Some(Cow::Owned("single value".to_string()))),
        vec!["single value"]
    )]
    #[case(
        Value::SingleLine(None),
        vec!["     "]
    )]
    #[case(
        Value::MultiLine(vec![
            Some(Cow::Owned("multi".to_string())),
            Some(Cow::Owned("value".to_string())),
            Some(Cow::Owned("attribute".to_string()))
        ]),
        vec!["multi", "value", "attribute"]
    )]
    #[case(
        Value::MultiLine(vec![
            Some(Cow::Owned("multi".to_string())),
            None,
            Some(Cow::Owned("attribute".to_string()))
        ]),
        vec!["multi", "     ", "attribute"]
    )]
    /// A value and a Vec<&str> evaluate as equal if the contents match.
    fn value_partialeq_vec_str_eq_is_eq(#[case] value: Value, #[case] v: Vec<&str>) {
        assert_eq!(value, v);
    }

    #[rstest]
    #[case(
        Value::SingleLine(Some(Cow::Owned("single value".to_string()))),
        vec!["multi", "value"]
    )]
    #[case(
        Value::SingleLine(Some(Cow::Owned("single value".to_string()))),
        vec!["other single value"]
    )]
    #[case(
        Value::MultiLine(vec![
            Some(Cow::Owned("multi".to_string())),
            Some(Cow::Owned("value".to_string())),
            Some(Cow::Owned("attribute".to_string()))
        ]),
        vec!["different", "multi", "value", "attribute"]
    )]
    /// A value and a Vec<&str> do not evaluate as equal if the contents differ.
    fn value_partialeq_vec_str_ne_is_ne(#[case] value: Value, #[case] v: Vec<&str>) {
        assert_ne!(value, v);
    }

    #[rstest]
    #[case(
        Value::SingleLine(Some(Cow::Owned("single value".to_string()))),
        vec![Some("single value")]
    )]
    #[case(
        Value::MultiLine(vec![
            Some(Cow::Owned("multi".to_string())),
            Some(Cow::Owned("value".to_string())),
            Some(Cow::Owned("attribute".to_string()))
        ]),
        vec![Some("multi"), Some("value"), Some("attribute")]
    )]
    #[case(
        Value::MultiLine(vec![Some(Cow::Owned("multi".to_string())), None, Some(Cow::Owned("attribute".to_string()))]),
        vec![Some("multi"), None, Some("attribute")]
    )]
    /// A value and a Vec<Option<&str>> evaluate as equal if the contents match.
    fn value_partialeq_vec_option_str_eq_is_eq(#[case] value: Value, #[case] v: Vec<Option<&str>>) {
        assert_eq!(value, v);
    }

    #[rstest]
    #[case(
        Value::SingleLine(Some(Cow::Owned("single value".to_string()))),
        vec![Some("multi"), Some("value")]
    )]
    #[case(
        Value::SingleLine(Some(Cow::Owned("single value".to_string()))),
        vec![Some("other single value")]
    )]
    #[case(
        Value::SingleLine(None),
        vec![Some("     ")]
    )]
    #[case(
        Value::MultiLine(vec![
            Some(Cow::Owned("multi".to_string())),
            Some(Cow::Owned("value".to_string())),
            Some(Cow::Owned("attribute".to_string()))
        ]),
        vec![Some("different"), Some("multi"), Some("value"), Some("attribute")]
    )]
    /// A value and a Vec<Option<&str>> do not evaluate as equal if the contents differ.
    fn value_partialeq_vec_option_str_ne_is_ne(#[case] value: Value, #[case] v: Vec<Option<&str>>) {
        assert_ne!(value, v);
    }

    #[rstest]
    #[case(
        Value::unchecked_single("single value"),
        vec![Some("single value".to_string())]
    )]
    #[case(
        Value::unchecked_multi(["multiple",  "values"]),
        vec![Some("multiple".to_string()),  Some("values".to_string())]
    )]
    #[case(
        Value::unchecked_multi(["multiple", "", "separated",  "values"]),
        vec![Some("multiple".to_string()), None, Some("separated".to_string()),  Some("values".to_string())]
    )]
    fn value_into_vec_of_option_str(#[case] value: Value, #[case] expected: Vec<Option<String>>) {
        let vec: Vec<Option<String>> = value.into();
        assert_eq!(vec, expected);
    }

    proptest! {
        #[test]
        fn value_from_str_non_ascii_is_err(v in r"[^[[:ascii:]]]") {
            assert!(Name::from_str(&v).is_err());
        }

        #[test]
        fn value_from_str_ascii_control_is_err(v in r"[[:cntrl:]]") {
            assert!(Name::from_str(&v).is_err());
        }
    }
}
