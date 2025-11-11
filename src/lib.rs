#![doc = include_str!("../README.md")]
#![cfg_attr(docsrs, feature(doc_cfg))]

pub use attribute::{Attribute, Name, Value};
pub use error::{AttributeError, ParseError};
pub use object::Object;
pub use parser::{parse_object, parse_whois_response};
pub use spec::Specification;

mod attribute;
#[allow(clippy::module_name_repetitions)]
mod error;
mod object;
mod parser;
mod spec;
