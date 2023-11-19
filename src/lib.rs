#![warn(clippy::pedantic)]
#![warn(missing_docs)]
#![forbid(unsafe_code)]
#![forbid(clippy::panic)]
#![doc = include_str!("../README.md")]

pub use parser::{parse_object, parse_whois_response};
pub use rpsl::{Attribute, AttributeError, Object};

mod parser;
mod rpsl;
