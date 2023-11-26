#[derive(Debug, PartialEq, Eq, Clone)]
pub struct NameView<'a>(&'a str);

impl<'a> NameView<'a> {
    pub(crate) fn new(name: &'a str) -> Self {
        Self(name)
    }
}

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
}

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct AttributeView<'a> {
    pub name: NameView<'a>,
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

fn coerce_empty_value(value: &str) -> Option<&str> {
    if value.trim().is_empty() {
        None
    } else {
        Some(value)
    }
}
