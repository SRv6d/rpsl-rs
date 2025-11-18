use std::{borrow::Cow, convert::Infallible, fmt, marker::PhantomData, ops::Deref, str::FromStr};

#[cfg(feature = "serde")]
use serde::Serialize;

use crate::{
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

#[cfg(test)]
impl<'a> Attribute<'a, Raw> {
    /// Test helper to create an attribute with a single line value.
    pub(crate) fn unchecked_single<V>(name: &'a str, value: V) -> Self
    where
        V: Into<Option<&'a str>>,
    {
        let name = Name::new(name);
        let value = match value.into() {
            Some(value) => Value::new_single(value),
            None => Value::new_single(String::new()),
        };
        Self { name, value }
    }

    /// Test helper to create an attribute with a multi line value.
    pub(crate) fn unchecked_multi<I, V>(name: &'a str, values: I) -> Self
    where
        I: IntoIterator<Item = V>,
        V: Into<Option<&'a str>>,
    {
        let name = Name::new(name);
        let collected: Vec<String> = values
            .into_iter()
            .map(|value| match value.into() {
                Some(value) => value.to_string(),
                None => String::new(),
            })
            .collect();
        let value = Value::new_multi(collected);
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

impl Name<'static, Raw> {
    /// Create a [`Name`].
    pub fn new<S>(name: S) -> Self
    where
        S: Into<String>,
    {
        Self {
            inner: Cow::Owned(name.into()),
            _spec: PhantomData,
        }
    }

}

impl<'a> Name<'a, Raw> {
    /// Create a name from parsed RPSL.
    pub(crate) fn from_parsed(name: &'a str) -> Self {
        Self {
            inner: Cow::Borrowed(name),
            _spec: PhantomData,
        }
    }
}

impl FromStr for Name<'static, Raw> {
    type Err = Infallible;

    /// Create a new [`Name`] from a string slice.
    fn from_str(name: &str) -> Result<Self, Self::Err> {
        Ok(Self::new(name))
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
        /// The value.
        inner: Option<Cow<'a, str>>,
        /// The values specification.
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
        /// The value.
        inner: Vec<Option<Cow<'a, str>>>,
        /// The values specification.
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

impl Value<'static, Raw> {
    /// Create a single line value. Empty values are coerced to [`None`].
    pub fn new_single<V>(value: V) -> Self
    where
        V: Into<String>,
    {
        Self::SingleLine {
            inner: coerce_empty_value(value.into()).map(Cow::Owned),
            _spec: PhantomData,
        }
    }

    /// Create a multi line value. Empty values are coerced to [`None`].
    ///
    /// # Panics
    /// If the given iterator contains less than two values.
    pub fn new_multi<I, V>(values: I) -> Self
    where
        I: IntoIterator<Item = V>,
        V: Into<String>,
    {
        let s = Self::MultiLine {
            inner: values
                .into_iter()
                .map(|v| coerce_empty_value(v.into()).map(Cow::Owned))
                .collect(),
            _spec: PhantomData,
        };
        assert!(s.lines() >= 2, "multi line values need at least two lines");
        s
    }
}

impl<'a> Value<'a, Raw> {
    /// Create a single line value from parsed RPSL. Empty values are coerced to [`None`].
    pub(crate) fn from_parsed_single(value: &'a str) -> Self
    {
        Self::SingleLine {
            inner: coerce_empty_value(value).map(Cow::Borrowed),
            _spec: PhantomData,
        }
    }

    /// Create a multi line value from parsed RPSL. Empty values are coerced to [`None`].
    /// 
    /// # Panics
    /// If the given iterator contains less than two values.
    pub(crate) fn from_parsed_multi<I>(values: I) -> Self
    where
        I: IntoIterator<Item = &'a str>,
    {
        let s = Self::MultiLine {
            inner: values
                .into_iter()
                .map(|v| coerce_empty_value(v).map(Cow::Borrowed))
                .collect(),
            _spec: PhantomData,
        };
        assert!(s.lines() >= 2, "multi line values need at least two lines");
        s
    }
}

impl FromStr for Value<'static, Raw> {
    type Err = Infallible;

    /// Create a new single line value from a string slice.
    fn from_str(value: &str) -> Result<Self, Self::Err> {
        Ok(Self::new_single(value))
    }
}

impl<S> From<Vec<S>> for Value<'static, Raw>
where 
    S: Into<String> 
{

    /// Create a new value from an iterator of value lines.
    ///
    /// # Example
    /// ```
    /// # use rpsl::Value;
    /// let value: Value = vec!["Packet Street 6", "128 Series of Tubes", "Internet"].into();
    /// assert_eq!(value.lines(), 3);
    /// ```
    fn from(values: Vec<S>) -> Self {
        let v: Vec<String> = values.into_iter().map(Into::into).collect();

        match v.len() {
            0 => Value::new_single(String::new()),
            1 => Value::new_single(v.into_iter().next().expect("vec has at least one value")),
            _ => Value::new_multi(v),
        }  
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

    #[rstest]
    #[case("Ref", Name { inner: Cow::Owned("Ref".to_string()), _spec: PhantomData })]
    fn name_new<S: Into<String>>(#[case] s: S, #[case] expected: Name<Raw>) {
        let attribute = Name::new(s);
        assert_eq!(attribute, expected);
    }

    #[test]
    fn name_display() {
        let name_display = Name::new("address").to_string();
        assert_eq!(name_display, "address");
    }

    #[rstest]
    #[case("role")]
    #[case("person")]
    fn name_deref(#[case] s: &str) {
        let name = Name::new(s);
        assert_eq!(*name, *s);
    }

    #[rstest]
    #[case("role")]
    #[case("person")]
    fn name_from_str(#[case] s: &str) {
        assert_eq!(Name::from_str(s).unwrap(), Name::new(s));
    }

    #[rstest]
    #[case(Name::new("ASNumber"), Token::Str("ASNumber"))]
    #[cfg(feature = "serde")]
    fn name_serialize(#[case] name: Name, #[case] expected: Token) {
        assert_ser_tokens(&name, &[expected]);
    }

    #[rstest]
    #[case(
        "This is a valid attribute value",
        Value::SingleLine {
            inner: Some(Cow::Owned("This is a valid attribute value".to_string())),
            _spec: PhantomData
        }
    )]
    fn value_new_single<S: Into<String>>(#[case] s: S, #[case] expected: Value<Raw>) {
        let attribute = Value::new_single(s);
        assert_eq!(attribute, expected);
    }

    #[rstest]
    #[case(
        vec!["Packet Street 6", "128 Series of Tubes", "Internet"],
        Value::MultiLine { 
            inner: vec![
                Some(Cow::Owned("Packet Street 6".to_string())),
                Some(Cow::Owned("128 Series of Tubes".to_string())),
                Some(Cow::Owned("Internet".to_string()))
            ], 
            _spec: PhantomData 
        }
    )]
    fn value_new_multi<I, V>(#[case] i: I, #[case] expected: Value<Raw>) 
    where 
        I: IntoIterator<Item = V>,
        V: Into<String>,
    {
        let attribute = Value::new_multi(i);
        assert_eq!(attribute, expected);
    }

    #[rstest]
    #[case("This is a valid attribute value", Value::new_single("This is a valid attribute value".to_string()))]
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
        Value::new_single("32934"),
        &[
            Token::Seq { len: Some(1) },
            Token::Some,
            Token::Str("32934"),
            Token::SeqEnd,
        ],
    )]
    #[case(
        Value::new_single(""),
        &[
            Token::Seq { len: Some(1) },
            Token::None,
            Token::SeqEnd,
        ],
    )]
    #[case(
        Value::new_multi(["Packet Street 6", "128 Series of Tubes", "Internet"]),
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
    #[case(
        Value::new_single(""),
        Value::SingleLine {
            inner: None,
            _spec: PhantomData
        }
    )]
    #[case(
        Value::new_single("   "),
        Value::SingleLine {
            inner: None,
            _spec: PhantomData
        }
    )]
    #[case(
        Value::new_multi(["", " ", "   "]),
        Value::MultiLine {
            inner: vec![None, None, None],
            _spec: PhantomData
        }
    )]
    /// Creating values from empty strings results in None values.
    fn value_new_empty_is_none(#[case] value: Value, #[case] expected: Value) {
        assert_eq!(value, expected);
    }

    #[test]
    #[should_panic(expected = "multi line values need at least two lines")]
    /// Multi line attributes cannot be created with only a single value.
    fn value_new_multi_with_single_value_panics() {
        Value::new_multi(["just one"]);
    }

    #[rstest]
    #[case(
        vec!["Packet Street 6"],
        Value::new_single("Packet Street 6")
    )]
    #[case(
        vec![],
        Value::new_single("")
    )]
    #[case(
        vec!["Packet Street 6", "128 Series of Tubes", "Internet"],
        Value::new_multi(vec![
            "Packet Street 6",
            "128 Series of Tubes",
            "Internet"
        ])
    )]
    #[case(
        vec!["", "128 Series of Tubes", "Internet"],
        Value::new_multi(vec![
            "",
            "128 Series of Tubes",
            "Internet"
        ])
    )]
    #[case(
        vec!["", " ", "   "],
        Value::new_multi(vec!["", "", ""])
    )]
    fn value_from_vec_of_str(#[case] v: Vec<&str>, #[case] expected: Value) {
        let value = Value::from(v);
        assert_eq!(value, expected);
    }

    #[rstest]
    #[case("single value", 1)]
    #[case(vec!["multi", "value", "attribute"].try_into().unwrap(), 3)]
    fn value_lines(#[case] value: Value, #[case] expected: usize) {
        assert_eq!(value.lines(), expected);
    }

    #[rstest]
    #[case(Value::new_single(""), vec![])]
    #[case(Value::new_single("single value"), vec!["single value"])]
    #[case(
        Value::new_multi(["", "128 Series of Tubes", "Internet"]),
        vec!["128 Series of Tubes", "Internet"]
    )]
    #[case(
        Value::new_multi(["Packet Street 6", "128 Series of Tubes", "Internet"]),
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
        let value = Value::new_single(s);
        assert_eq!(value, s);
    }

    #[rstest]
    #[case(Value::new_single("a value"), "a different value")]
    #[case(
        Value::new_multi([
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
        Value::new_single("single value"),
        vec!["single value"]
    )]
    #[case(
        Value::new_single(""),
        vec!["     "]
    )]
    #[case(
        Value::new_multi([
            "multi",
            "value",
            "attribute"
        ]),
        vec!["multi", "value", "attribute"]
    )]
    #[case(
        Value::new_multi(["multi", "", "attribute"]),
        vec!["multi", "     ", "attribute"]
    )]
    /// A value and a Vec<&str> evaluate as equal if the contents match.
    fn value_partialeq_vec_str_eq_is_eq(#[case] value: Value, #[case] v: Vec<&str>) {
        assert_eq!(value, v);
    }

    #[rstest]
    #[case(Value::new_single("single value"), vec!["multi", "value"])]
    #[case(
        Value::new_single("single value"),
        vec!["other single value"]
    )]
    #[case(
        Value::new_multi(["multi", "value", "attribute"]),
        vec!["different", "multi", "value", "attribute"]
    )]
    /// A value and a Vec<&str> do not evaluate as equal if the contents differ.
    fn value_partialeq_vec_str_ne_is_ne(#[case] value: Value, #[case] v: Vec<&str>) {
        assert_ne!(value, v);
    }

    #[rstest]
    #[case(Value::new_single("single value"), vec![Some("single value")])]
    #[case(
        Value::new_multi(["multi", "value", "attribute"]),
        vec![Some("multi"), Some("value"), Some("attribute")]
    )]
    #[case(
        Value::new_multi(["multi", "", "attribute"]),
        vec![Some("multi"), None, Some("attribute")]
    )]
    /// A value and a Vec<Option<&str>> evaluate as equal if the contents match.
    fn value_partialeq_vec_option_str_eq_is_eq(#[case] value: Value, #[case] v: Vec<Option<&str>>) {
        assert_eq!(value, v);
    }

    #[rstest]
    #[case(
        Value::new_single("single value"),
        vec![Some("multi"), Some("value")]
    )]
    #[case(
        Value::new_single("single value"),
        vec![Some("other single value")]
    )]
    #[case(Value::new_single(""), vec![Some("     ")])]
    #[case(
        Value::new_multi(["multi", "value", "attribute"]),
        vec![Some("different"), Some("multi"), Some("value"), Some("attribute")]
    )]
    /// A value and a Vec<Option<&str>> do not evaluate as equal if the contents differ.
    fn value_partialeq_vec_option_str_ne_is_ne(#[case] value: Value, #[case] v: Vec<Option<&str>>) {
        assert_ne!(value, v);
    }

    #[rstest]
    #[case(
        Value::new_single("single value"),
        vec![Some("single value".to_string())]
    )]
    #[case(
        Value::new_multi(["multiple", "values"]),
        vec![Some("multiple".to_string()), Some("values".to_string())]
    )]
    #[case(
        Value::new_multi(["multiple", "", "separated", "values"]),
        vec![
            Some("multiple".to_string()),
            None,
            Some("separated".to_string()),
            Some("values".to_string())
        ]
    )]
    fn value_into_vec_of_option_string(
        #[case] value: Value,
        #[case] expected: Vec<Option<String>>,
    ) {
        let vec: Vec<Option<String>> = value.into();
        assert_eq!(vec, expected);
    }
}
