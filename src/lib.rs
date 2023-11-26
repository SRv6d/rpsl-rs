#![warn(clippy::pedantic)]
#![warn(missing_docs)]
#![forbid(unsafe_code)]
#![forbid(clippy::panic)]
#![doc = include_str!("../README.md")]

pub use parser::{parse_object, parse_whois_response};
pub use rpsl::error::AttributeError;
pub use rpsl::{AttributeView, ObjectView};

mod parser;
mod rpsl;
