use super::attribute::AttributeView;

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct ObjectView<'a> {
    pub attributes: Vec<AttributeView<'a>>,
}

impl<'a> ObjectView<'a> {
    pub(crate) fn new(attributes: Vec<AttributeView<'a>>) -> Self {
        Self { attributes }
    }
}
