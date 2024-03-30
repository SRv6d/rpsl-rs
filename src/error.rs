use std::fmt;
use thiserror::Error;

#[derive(Error, Debug)]
/// An error that occurs if invalid RPSL syntax is encountered.
pub struct SyntaxError<'a> {
    loc: &'a str,
    /// The line number containing the syntax error.
    pub line: usize,
}

impl fmt::Display for SyntaxError<'_> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Syntax error in line {}: {}", self.line, self.loc)
    }
}

#[derive(Error, Debug)]
pub enum InvalidNameError {
    #[error("cannot be empty")]
    Empty,
    #[error("cannot contain non-ASCII characters")]
    NonAscii,
    #[error("cannot start with a non-letter ASCII character")]
    NonAsciiAlphabeticFirstChar,
    #[error("cannot end with a non-letter or non-digit ASCII character")]
    NonAsciiAlphanumericLastChar,
}

#[derive(Error, Debug)]
pub enum InvalidValueError {
    #[error("cannot contain non-ASCII characters")]
    NonAscii,
    #[error("cannot contain ASCII control characters")]
    ContainsControlChar,
}
