use winnow::stream::ContainsToken;

#[derive(Debug, Default)]
pub struct Spec {
    value: ValueSpec,
}

#[derive(Debug, Default)]
pub(crate) enum ValueSpec {
    // ASCII characters, excluding control.
    #[default]
    Rfc2622,
}

impl ContainsToken<char> for ValueSpec {
    fn contains_token(&self, char: char) -> bool {
        match self {
            Self::Rfc2622 => char.is_ascii() && !char.is_ascii_control(),
        }
    }
}
