#![warn(clippy::pedantic)]
#![warn(missing_docs)]
#![forbid(unsafe_code)]
#![forbid(clippy::panic)]
#![doc = include_str!("../README.md")]

pub use error::AttributeError;
pub use parser::{parse_object, parse_whois_response};

pub use self::borrowed::{AttributeView, ObjectView};
pub use self::owned::{Attribute, Object};
pub(crate) use self::owned::{Name, Value};

mod borrowed;
mod common;
#[allow(clippy::module_name_repetitions)]
mod error;
mod owned;
mod parser;
