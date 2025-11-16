use std::{borrow::Cow, convert::Infallible, fmt, marker::PhantomData, ops::Deref, str::FromStr};

#[cfg(feature = "serde")]
use serde::Serialize;

use crate::{
    error::{InvalidNameError, InvalidValueError},
    spec::{Raw, Specification},
};

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
#[cfg_attr(feature = "serde", derive(Serialize), serde(bound = ""))]
pub struct Attribute<'a, S: Specification = Raw> {
    /// The name of the attribute.
    pub name: Name<'a, S>,
    /// The value of the attribute.
    #[cfg_attr(feature = "serde", serde(rename = "values"))]
    pub value: Value<'a, S>,
}

impl<'a, S: Specification> Attribute<'a, S> {
    /// Create a new attribute.
    #[must_use]
    pub fn new(name: Name<'a, S>, value: Value<'a, S>) -> Self {
        Self { name, value }
    }
}

impl<'a> Attribute<'a, Raw> {
    #[cfg(test)]
    pub(crate) fn unchecked_single<V>(name: &'a str, value: V) -> Self
    where
        V: Into<Option<&'a str>>,
    {
        let name = Name::unchecked(name);
        let value = Value::unchecked_single(value);
        Self { name, value }
    }

    #[cfg(test)]
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

impl<S: Specification> fmt::Display for Attribute<'_, S> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let values = self.value.values();

        let first_value = values.first().expect("must contain at least one value");
        match first_value {
            Some(value) => {
                writeln!(f, "{:16}{}", format!("{}:", self.name), value)?;
            }
            None => writeln!(f, "{}:", self.name)?,
        }

        let remaining_values = &values[1..];
        for value in remaining_values {
            match value {
                Some(value) => {
                    writeln!(f, "{:16}{}", " ", value)?;
                }
                None => {
                    writeln!(f, " ")?;
                }
            }
        }

        Ok(())
    }
}

/// The name of an [`Attribute`].
#[derive(Debug, PartialEq, Eq, Clone)]
#[cfg_attr(feature = "serde", derive(Serialize), serde(transparent))]
pub struct Name<'a, S: Specification = Raw> {
    inner: Cow<'a, str>,
    #[cfg_attr(feature = "serde", serde(skip))]
    _spec: PhantomData<S>,
}

impl<'a> Name<'a, Raw> {
    pub(crate) fn unchecked(name: &'a str) -> Self {
        Self {
            inner: Cow::Borrowed(name),
            _spec: PhantomData,
        }
    }
}

impl<S: Specification> FromStr for Name<'_, S> {
    type Err = InvalidNameError;

    /// Create a new `Name` from a string slice.
    ///
    /// A valid name may consist of ASCII letters, digits and the characters "-", "_",
    /// while beginning with a letter and ending with a letter or a digit.
    ///
    /// # Errors
    /// Returns an error if the name is empty or invalid.
    fn from_str(name: &str) -> Result<Self, Self::Err> {
        todo!()
    }
}

impl<S: Specification> Deref for Name<'_, S> {
    type Target = str;

    fn deref(&self) -> &Self::Target {
        self.inner.as_ref()
    }
}

impl<S: Specification> PartialEq<&str> for Name<'_, S> {
    fn eq(&self, other: &&str) -> bool {
        self.inner == *other
    }
}

impl<S: Specification> fmt::Display for Name<'_, S> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.inner)
    }
}

/// The value of an [`Attribute`].
/// Since only some values contain multiple lines and single line values do not require
/// additional heap allocation, an Enum is used to represent both variants.
#[derive(Debug, PartialEq, Eq, Clone)]
#[cfg_attr(
    feature = "serde",
    derive(Serialize),
    serde(into = "Vec<Option<String>>")
)]
pub enum Value<'a, S: Specification = Raw> {
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
    SingleLine {
        inner: Option<Cow<'a, str>>,
        #[cfg_attr(feature = "serde", serde(skip))]
        _spec: PhantomData<S>,
    },
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
    MultiLine {
        inner: Vec<Option<Cow<'a, str>>>,
        #[cfg_attr(feature = "serde", serde(skip))]
        _spec: PhantomData<S>,
    },
}

impl<'a, S: Specification> Value<'a, S> {
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
            Self::SingleLine { .. } => 1,
            Self::MultiLine { inner, .. } => inner.len(),
        }
    }

    fn values(&'a self) -> Vec<Option<&'a str>> {
        match self {
            Value::SingleLine { inner, .. } => {
                vec![inner.as_ref().map(std::convert::AsRef::as_ref)]
            }
            Value::MultiLine { inner, .. } => inner
                .iter()
                .map(|v| v.as_ref().map(std::convert::AsRef::as_ref))
                .collect(),
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
            Self::SingleLine { inner, .. } => {
                if let Some(inner) = inner {
                    vec![inner]
                } else {
                    vec![]
                }
            }
            Self::MultiLine { inner, .. } => inner.iter().flatten().map(AsRef::as_ref).collect(),
        }
    }
}

impl<'a> Value<'a, Raw> {
    /// Create a single line value without checking that characters conform to any specification
    /// while still coercing empty values to `None`.
    pub(crate) fn unchecked_single<V>(value: V) -> Self
    where
        V: Into<Option<&'a str>>,
    {
        Self::SingleLine {
            inner: value.into().and_then(coerce_empty_value).map(Cow::Borrowed),
            _spec: PhantomData,
        }
    }

    /// Create a multi line value without checking that characters conform to any specification
    /// while still coercing empty values to `None`.
    pub(crate) fn unchecked_multi<I, V>(values: I) -> Self
    where
        I: IntoIterator<Item = V>,
        V: Into<Option<&'a str>>,
    {
        let s = Self::MultiLine {
            inner: values
                .into_iter()
                .map(|v| v.into().and_then(coerce_empty_value).map(Cow::Borrowed))
                .collect(),
            _spec: PhantomData,
        };
        assert!(s.lines() > 1, "multi line values need at least two lines");
        s
    }
}

impl FromStr for Value<'_, Raw> {
    type Err = Infallible;

    /// Create a new single line value from a string slice.
    fn from_str(value: &str) -> Result<Self, Self::Err> {
        Ok(Self::SingleLine {
            inner: coerce_empty_value(value).map(|value| Cow::Owned(value.to_string())),
            _spec: PhantomData,
        })
    }
}

// TODO: Turn into From<Vec<&str>>
impl TryFrom<Vec<&str>> for Value<'_, Raw> {
    type Error = Infallible;

    /// Create a new value from a vector of string slices, representing the values lines.
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
            .map(|v| Ok(coerce_empty_value(v).map(std::string::ToString::to_string)))
            .collect::<Result<Vec<Option<String>>, Infallible>>()?;

        Ok(Self::MultiLine {
            inner: values.into_iter().map(|v| v.map(Cow::Owned)).collect(),
            _spec: PhantomData,
        })
    }
}

impl<'a, S: Specification> From<Value<'a, S>> for Vec<Option<String>> {
    fn from(value: Value<'a, S>) -> Self {
        match value {
            Value::SingleLine { inner, .. } => vec![inner.map(|v| v.to_string())],
            Value::MultiLine { inner, .. } => inner
                .into_iter()
                .map(|v| v.map(|v| v.to_string()))
                .collect(),
        }
    }
}

impl<S: Specification> PartialEq<&str> for Value<'_, S> {
    fn eq(&self, other: &&str) -> bool {
        match &self {
            Self::MultiLine { .. } => false,
            Self::SingleLine { inner, .. } => match inner {
                Some(value) => value == *other,
                None => coerce_empty_value(other).is_none(),
            },
        }
    }
}

impl<S: Specification> PartialEq<Vec<&str>> for Value<'_, S> {
    fn eq(&self, other: &Vec<&str>) -> bool {
        if self.lines() != other.len() {
            return false;
        }

        match &self {
            Self::SingleLine { inner, .. } => {
                let s = inner.as_deref();
                let other_coerced = coerce_empty_value(other[0]);
                s == other_coerced
            }
            Self::MultiLine { inner, .. } => {
                let s = inner.iter().map(|v| v.as_deref());
                let other_coerced = other.iter().map(|&v| coerce_empty_value(v));
                s.eq(other_coerced)
            }
        }
    }
}

impl<S: Specification> PartialEq<Vec<Option<&str>>> for Value<'_, S> {
    fn eq(&self, other: &Vec<Option<&str>>) -> bool {
        if self.lines() != other.len() {
            return false;
        }

        match &self {
            Self::SingleLine { inner, .. } => {
                let s = inner.as_deref();
                let other = other[0];
                s == other
            }
            Self::MultiLine { inner, .. } => {
                let s = inner.iter().map(|v| v.as_deref());
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
    use rstest::*;
    #[cfg(feature = "serde")]
    use serde_test::{assert_ser_tokens, Token};

    use super::*;

    #[rstest]
    #[case(
        Attribute::unchecked_single("ASNumber", "32934"),
        "ASNumber:       32934\n"
    )]
    #[case(Attribute::unchecked_single("ASNumber", None), "ASNumber:\n")]
    #[case(
        Attribute::unchecked_single("ASName", "FACEBOOK"),
        "ASName:         FACEBOOK\n"
    )]
    #[case(
        Attribute::unchecked_single("RegDate", "2004-08-24"),
        "RegDate:        2004-08-24\n"
    )]
    #[case(
        Attribute::unchecked_single("Ref", "https://rdap.arin.net/registry/autnum/32934"),
        "Ref:            https://rdap.arin.net/registry/autnum/32934\n"
    )]
    fn attribute_display_single_line<S: Specification>(
        #[case] attribute: Attribute<S>,
        #[case] expected: &str,
    ) {
        assert_eq!(attribute.to_string(), expected);
    }

    #[rstest]
    #[case(
        Attribute::unchecked_multi(
            "remarks",
            [
                "AS1299 is matching RPKI validation state and reject",
                "invalid prefixes from peers and customers."
            ]

        ),
        concat!(
            "remarks:        AS1299 is matching RPKI validation state and reject\n",
            "                invalid prefixes from peers and customers.\n",
        )
    )]
    #[case(
        Attribute::unchecked_multi(
            "remarks",
            [
                None,
                None
            ]
        ),
        concat!(
            "remarks:\n",
            " \n",
        )
    )]
    fn attribute_display_multi_line<S: Specification>(
        #[case] attribute: Attribute<S>,
        #[case] expected: &str,
    ) {
        assert_eq!(attribute.to_string(), expected);
    }

    #[rstest]
    #[case(
        Attribute::unchecked_single("ASNumber", "32934"),
        &[
            Token::Struct { name: "Attribute", len: 2 },
            Token::Str("name"),
            Token::Str("ASNumber"),
            Token::Str("values"),
            Token::Seq { len: Some(1) },
            Token::Some,
            Token::Str("32934"),
            Token::SeqEnd,
            Token::StructEnd,
        ],
    )]
    #[case(
        Attribute::unchecked_multi(
            "address",
            ["Packet Street 6", "128 Series of Tubes", "Internet"]
        ),
        &[
            Token::Struct { name: "Attribute", len: 2 },
            Token::Str("name"),
            Token::Str("address"),
            Token::Str("values"),
            Token::Seq { len: Some(3) },
            Token::Some,
            Token::Str("Packet Street 6"),
            Token::Some,
            Token::Str("128 Series of Tubes"),
            Token::Some,
            Token::Str("Internet"),
            Token::SeqEnd,
            Token::StructEnd,
        ],
    )]
    #[cfg(feature = "serde")]
    fn attribute_serialize<S: Specification>(
        #[case] attribute: Attribute<S>,
        #[case] expected: &[Token],
    ) {
        assert_ser_tokens(&attribute, expected);
    }

    #[test]
    fn name_display() {
        let name_display = Name::unchecked("address").to_string();
        assert_eq!(name_display, "address");
    }

    #[rstest]
    #[case("role")]
    #[case("person")]
    fn name_deref(#[case] s: &str) {
        let name = Name::unchecked(s);
        assert_eq!(*name, *s);
    }

    #[rstest]
    #[case("role")]
    #[case("person")]
    fn name_from_str(#[case] s: &str) {
        assert_eq!(Name::from_str(s).unwrap(), Name(Cow::Owned(s.to_string())));
    }

    #[rstest]
    #[case(Name::unchecked("ASNumber"), Token::Str("ASNumber"))]
    #[cfg(feature = "serde")]
    fn name_serialize(#[case] name: Name, #[case] expected: Token) {
        assert_ser_tokens(&name, &[expected]);
    }

    #[rstest]
    #[case("This is a valid attribute value", Value::SingleLine(Some(Cow::Owned("This is a valid attribute value".to_string()))))]
    fn value_from_str(#[case] s: &str, #[case] expected: Value) {
        assert_eq!(Value::from_str(s).unwrap(), expected);
    }

    #[rstest]
    fn value_from_empty_str(#[values("", "   ")] s: &str) {
        let expected = Value::SingleLine {
            inner: None,
            _spec: PhantomData,
        };
        assert_eq!(Value::from_str(s).unwrap(), expected);
    }

    #[rstest]
    #[case(
        Value::unchecked_single("32934"),
        &[
            Token::Seq { len: Some(1) },
            Token::Some,
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
            Token::Some,
            Token::Str("Packet Street 6"),
            Token::Some,
            Token::Str("128 Series of Tubes"),
            Token::Some,
            Token::Str("Internet"),
            Token::SeqEnd,
        ],
    )]
    #[cfg(feature = "serde")]
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

    // #[rstest]
    // #[case(
    //     vec!["Packet Street 6", "128 Series of Tubes", "Internet"],
    //     Value::MultiLine(vec![
    //         Some(Cow::Owned("Packet Street 6".to_string())),
    //         Some(Cow::Owned("128 Series of Tubes".to_string())),
    //         Some(Cow::Owned("Internet".to_string()))
    //     ])
    // )]
    // #[case(
    //     vec!["", "128 Series of Tubes", "Internet"],
    //     Value::MultiLine(vec![
    //         None,
    //         Some(Cow::Owned("128 Series of Tubes".to_string())),
    //         Some(Cow::Owned("Internet".to_string()))
    //     ])
    // )]
    // #[case(
    //     vec!["", " ", "   "],
    //     Value::MultiLine(vec![None, None, None])
    // )]
    // fn value_from_vec_of_str(#[case] v: Vec<&str>, #[case] expected: Value) {
    //     let value = Value::try_from(v).unwrap();
    //     assert_eq!(value, expected);
    // }

    // #[test]
    // fn value_from_vec_w_1_value_is_single_line() {
    //     assert_eq!(
    //         Value::try_from(vec!["Packet Street 6"]).unwrap(),
    //         Value::SingleLine(Some(Cow::Owned("Packet Street 6".to_string())))
    //     );
    // }

    #[rstest]
    #[case("single value", 1)]
    #[case(vec!["multi", "value", "attribute"].try_into().unwrap(), 3)]
    fn value_lines(#[case] value: Value, #[case] expected: usize) {
        assert_eq!(value.lines(), expected);
    }

    #[rstest]
    #[case(
        Value::unchecked_single(None),
        vec![]
    )]
    #[case(
        Value::unchecked_single("single value"),
        vec!["single value"]
    )]
    #[case(
        Value::unchecked_multi(vec![
            None,
            Some("128 Series of Tubes"),
            Some("Internet"),
        ]),
        vec!["128 Series of Tubes", "Internet"]
    )]
    #[case(
        Value::unchecked_multi([
            "Packet Street 6",
            "128 Series of Tubes",
            "Internet"
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
        let value = Value::unchecked_single(s);
        assert_eq!(value, s);
    }

    #[rstest]
    #[case(Value::unchecked_single("a value"), "a different value")]
    #[case(
        Value::unchecked_multi([
            "multi",
            "value"
        ]),
       "single value"
    )]
    /// A value and &str do not evaluate as equal if the contents differ.
    fn value_partialeq_str_ne_is_ne(#[case] value: Value, #[case] s: &str) {
        assert_ne!(value, s);
    }

    #[rstest]
    #[case(
        Value::unchecked_single("single value"),
        vec!["single value"]
    )]
    #[case(
        Value::unchecked_single(None),
        vec!["     "]
    )]
    #[case(
        Value::unchecked_multi([
            "multi",
            "value",
            "attribute"
        ]),
        vec!["multi", "value", "attribute"]
    )]
    #[case(
        Value::unchecked_multi([
            Some("multi"),
            None,
            Some("attribute")
        ]),
        vec!["multi", "     ", "attribute"]
    )]
    /// A value and a Vec<&str> evaluate as equal if the contents match.
    fn value_partialeq_vec_str_eq_is_eq(#[case] value: Value, #[case] v: Vec<&str>) {
        assert_eq!(value, v);
    }

    #[rstest]
    #[case(
        Value::unchecked_single("single value"),
        vec!["multi", "value"]
    )]
    #[case(
        Value::unchecked_single("single value"),
        vec!["other single value"]
    )]
    #[case(
        Value::unchecked_multi([
            "multi",
            "value",
            "attribute"
        ]),
        vec!["different", "multi", "value", "attribute"]
    )]
    /// A value and a Vec<&str> do not evaluate as equal if the contents differ.
    fn value_partialeq_vec_str_ne_is_ne(#[case] value: Value, #[case] v: Vec<&str>) {
        assert_ne!(value, v);
    }

    #[rstest]
    #[case(
        Value::unchecked_single("single value"),
        vec![Some("single value")]
    )]
    #[case(
        Value::unchecked_multi([
            "multi",
            "value",
            "attribute"
        ]),
        vec![Some("multi"), Some("value"), Some("attribute")]
    )]
    #[case(
        Value::unchecked_multi([Some("multi"), None, Some("attribute")]),
        vec![Some("multi"), None, Some("attribute")]
    )]
    /// A value and a Vec<Option<&str>> evaluate as equal if the contents match.
    fn value_partialeq_vec_option_str_eq_is_eq(#[case] value: Value, #[case] v: Vec<Option<&str>>) {
        assert_eq!(value, v);
    }

    #[rstest]
    #[case(
        Value::unchecked_single("single value"),
        vec![Some("multi"), Some("value")]
    )]
    #[case(
        Value::unchecked_single("single value"),
        vec![Some("other single value")]
    )]
    #[case(
        Value::unchecked_single(None),
        vec![Some("     ")]
    )]
    #[case(
        Value::unchecked_multi([
            "multi",
            "value",
            "attribute"
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
    fn value_into_vec_of_option_string(
        #[case] value: Value,
        #[case] expected: Vec<Option<String>>,
    ) {
        let vec: Vec<Option<String>> = value.into();
        assert_eq!(vec, expected);
    }
}
