use thiserror::Error;

#[derive(Error, Debug)]
pub enum InvalidNameError {
    #[error("cannot be empty")]
    Empty,
}

#[derive(Error, Debug)]
/// An error that can occur when parsing or trying to create an attribute that is invalid.
pub enum AttributeError {
    /// The name of the attribute is invalid.
    #[error("Invalid attribute name: {0}")]
    InvalidName(InvalidNameError),
}

impl From<InvalidNameError> for AttributeError {
    fn from(error: InvalidNameError) -> Self {
        AttributeError::InvalidName(error)
    }
}
