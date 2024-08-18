#![warn(clippy::pedantic)]
#![warn(missing_docs)]
#![forbid(unsafe_code)]
#![forbid(clippy::panic)]
#![doc = include_str!("../README.md")]

pub use error::AttributeError;
pub use parser::{parse_object, parse_whois_response};

pub use attribute::Attribute;
pub(crate) use attribute::{Name, Value};
pub use object::Object;

mod attribute;
mod common;
#[allow(clippy::module_name_repetitions)]
mod error;
mod object;
mod parser;
