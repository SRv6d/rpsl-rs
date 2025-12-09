#![doc = include_str!("../README.md")]
#![cfg_attr(docsrs, feature(doc_cfg))]

pub use attribute::{Attribute, Name, Value};
pub use object::Object;
pub use parser::{parse_object, parse_whois_response, ParseError};
pub use spec::{AttributeError, Specification};

mod attribute;
mod object;
mod parser;
pub mod spec;
