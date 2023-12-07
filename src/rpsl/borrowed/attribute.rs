use crate::rpsl::common::coerce_empty_value;

/// A type containing a string slice pointing to the name of an attribute.
#[derive(Debug, PartialEq, Eq, Clone)]
pub struct NameView<'a>(&'a str);

impl<'a> NameView<'a> {
    pub(crate) fn new(name: &'a str) -> Self {
        Self(name)
    }
}

impl PartialEq<&str> for NameView<'_> {
    fn eq(&self, other: &&str) -> bool {
        self.0 == *other
    }
}

/// A type containing a string slice pointing to the value of an attribute.
#[derive(Debug, PartialEq, Eq, Clone)]
pub enum ValueView<'a> {
    SingleLine(Option<&'a str>),
    MultiLine(Vec<Option<&'a str>>),
}

impl<'a> ValueView<'a> {
    pub(crate) fn new_single(value: &'a str) -> Self {
        Self::SingleLine(coerce_empty_value(value))
    }
    pub(crate) fn new_multi(values: Vec<&'a str>) -> Self {
        Self::MultiLine(values.into_iter().map(coerce_empty_value).collect())
    }
    /// The number of values referenced within the view.
    pub fn len(&self) -> usize {
        match &self {
            ValueView::SingleLine(_) => 1,
            ValueView::MultiLine(values) => values.len(),
        }
    }
}

impl<'a> IntoIterator for ValueView<'a> {
    type Item = Option<&'a str>;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        match self {
            Self::SingleLine(value) => vec![value].into_iter(),
            Self::MultiLine(values) => values.into_iter(),
        }
    }
}

impl PartialEq<&str> for ValueView<'_> {
    fn eq(&self, other: &&str) -> bool {
        match self {
            ValueView::MultiLine(_) => false,
            ValueView::SingleLine(value) => match value {
                Some(value) => value == other,
                None => coerce_empty_value(other).is_none(),
            },
        }
    }
}

impl PartialEq<Vec<&str>> for ValueView<'_> {
    fn eq(&self, other: &Vec<&str>) -> bool {
        match self {
            ValueView::SingleLine(_) => false,
            ValueView::MultiLine(values) => {
                if values.len() != other.len() {
                    return false;
                }
                for (s, o) in values.iter().zip(other.iter()) {
                    match s {
                        Some(value) => {
                            if value != o {
                                return false;
                            }
                        }
                        None => {
                            if coerce_empty_value(o).is_some() {
                                return false;
                            }
                        }
                    }
                }
                true
            }
        }
    }
}

impl PartialEq<Vec<Option<&str>>> for ValueView<'_> {
    fn eq(&self, other: &Vec<Option<&str>>) -> bool {
        match self {
            ValueView::SingleLine(_) => false,
            ValueView::MultiLine(values) => {
                if values.len() != other.len() {
                    return false;
                }

                for (s, o) in values.iter().zip(other.iter()) {
                    if s != o {
                        return false;
                    }
                }
                true
            }
        }
    }
}

/// A view into an attribute of an RPSL object in textual representation somewhere in memory.
#[derive(Debug, PartialEq, Eq, Clone)]
pub struct AttributeView<'a> {
    /// The name of the referenced attribute.
    pub name: NameView<'a>,
    /// The value of the referenced attribute.
    pub value: ValueView<'a>,
}

impl<'a> AttributeView<'a> {
    pub(crate) fn new_single(name: &'a str, value: &'a str) -> Self {
        let name = NameView::new(name);
        let value = ValueView::new_single(value);
        Self { name, value }
    }

    pub(crate) fn new_multi(name: &'a str, values: Vec<&'a str>) -> Self {
        let name = NameView::new(name);
        let value = ValueView::new_multi(values);
        Self { name, value }
    }
}

mod test {
    use super::*;

    #[test]
    fn value_len() {
        assert_eq!(ValueView::new_single("single value").len(), 1);
        assert_eq!(
            ValueView::new_multi(vec!["multi", "value", "attribute"]).len(),
            3
        );
    }

    #[test]
    fn value_eq_is_eq() {
        assert_eq!(ValueView::SingleLine(Some("single value")), "single value");
        assert_eq!(ValueView::SingleLine(None), " ");
        assert_eq!(
            ValueView::MultiLine(vec![Some("multi"), Some("value"), Some("attribute")]),
            vec!["multi", "value", "attribute"]
        );
        assert_eq!(
            ValueView::MultiLine(vec![Some("multi"), None, Some("attribute")]),
            vec!["multi", "    ", "attribute"]
        );
        assert_eq!(
            ValueView::MultiLine(vec![Some("multi"), Some("value"), Some("attribute")]),
            vec![Some("multi"), Some("value"), Some("attribute")]
        );
        assert_eq!(
            ValueView::MultiLine(vec![Some("multi"), None, Some("attribute")]),
            vec![Some("multi"), None, Some("attribute")]
        );
    }

    #[test]
    fn value_ne_is_ne() {
        assert_ne!(
            ValueView::SingleLine(Some("single value")),
            "other single value"
        );
        assert_ne!(ValueView::SingleLine(None), "not none");
        assert_ne!(
            ValueView::SingleLine(Some("single value")),
            vec!["other", "multi", "value", "attribute"]
        );
        assert_ne!(
            ValueView::MultiLine(vec![Some("multi"), Some("value"), Some("attribute")]),
            vec!["other", "multi", "value", "attribute"]
        );
        assert_ne!(
            ValueView::MultiLine(vec![Some("multi"), Some("value"), Some("attribute")]),
            vec![Some("multi"), None, Some("attribute")]
        );
        assert_ne!(
            ValueView::MultiLine(vec![Some("multi"), None, Some("attribute")]),
            vec![Some("multi"), Some("    "), Some("attribute")]
        );
    }
}
