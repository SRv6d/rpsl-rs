#![warn(clippy::pedantic)]
#![warn(missing_docs)]
#![forbid(unsafe_code)]
#![forbid(clippy::panic)]
#![doc = include_str!("../README.md")]

pub use error::{AttributeError, ParseError};
pub use parser::{parse_object, parse_whois_response};

pub use attribute::Attribute;
pub use object::Object;

mod attribute;
#[allow(clippy::module_name_repetitions)]
mod error;
mod object;
mod parser;
