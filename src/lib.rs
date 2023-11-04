#![warn(clippy::pedantic)]
#![warn(missing_docs)]
#![forbid(unsafe_code)]
#![doc = include_str!("../README.md")]

pub use parser::parse_object;
pub use rpsl::{Attribute, Object};

mod parser;
#[cfg(feature = "pyo3")]
mod pyo3;
mod rpsl;
