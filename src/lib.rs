#![warn(clippy::pedantic)]
#![warn(missing_docs)]
#![forbid(unsafe_code)]
#![doc = include_str!("../README.md")]

pub use parser::{parse_rpsl_object, parse_whois_server_response};
mod parser;
mod pyo3;
pub mod rpsl;
