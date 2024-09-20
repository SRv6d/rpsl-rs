use winnow::stream::ContainsToken;

#[derive(Default)]
pub struct Spec {
    name: NameSpec,
    value: ValueSpec,
}

pub(crate) struct NameSpec {
    chars: Box<dyn ContainsToken<char>>,
}

impl NameSpec {
    pub fn rfc_2622() -> Self {
        Self {
            chars: Box::new(('A'..='Z', 'a'..='z', '0'..='9', '-', '_')),
        }
    }
}

impl ContainsToken<char> for NameSpec {
    fn contains_token(&self, char: char) -> bool {
        self.chars.contains_token(char)
    }
}

impl Default for NameSpec {
    fn default() -> Self {
        Self::rfc_2622()
    }
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
