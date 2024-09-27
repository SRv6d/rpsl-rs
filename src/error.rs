use std::fmt;

use thiserror::Error;

#[derive(Error, Debug)]
pub enum InvalidNameError {
    #[error("cannot be empty")]
    Empty,
    #[error("cannot contain characters that are not part of the extended ASCII set")]
    NonAscii,
    #[error("cannot start with a non-letter ASCII character")]
    NonAsciiAlphabeticFirstChar,
    #[error("cannot end with a non-letter or non-digit ASCII character")]
    NonAsciiAlphanumericLastChar,
}

#[derive(Error, Debug)]
pub enum InvalidValueError {
    #[error("cannot contain characters that are not part of the extended ASCII set")]
    NonExtendedAscii,
    #[error("cannot contain ASCII control characters")]
    ContainsControlChar,
}

#[derive(Error, Debug)]
/// An error that can occur when parsing or trying to create an attribute that is invalid.
pub enum AttributeError {
    /// The name of the attribute is invalid.
    #[error("Invalid attribute name: {0}")]
    InvalidName(#[from] InvalidNameError),
    /// The value of the attribute is invalid.
    #[error("Invalid attribute value: {0}")]
    InvalidValue(#[from] InvalidValueError),
}

/// An error that can occur when parsing RPSL text.
#[derive(Error, Debug)]
pub struct ParseError(String);

impl fmt::Display for ParseError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.0)
    }
}

impl From<winnow::error::ParseError<&str, winnow::error::ContextError>> for ParseError {
    fn from(value: winnow::error::ParseError<&str, winnow::error::ContextError>) -> Self {
        Self(value.to_string())
    }
}
