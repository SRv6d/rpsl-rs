use std::fmt;

use thiserror::Error;

/// An error that can occur when parsing RPSL text.
///
/// # Example
/// ```
/// # use rpsl::parse_object;
/// let rpsl = "\
/// role;        ACME Company
///
/// ";
/// let err = parse_object(rpsl).unwrap_err();
/// let message = "\
/// parse error at line 1, column 5
///   |
/// 1 | role;        ACME Company
///   |     ^
/// invalid separator
/// expected `:`";
/// assert_eq!(err.to_string(), message);
/// ```
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
