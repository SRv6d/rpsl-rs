pub use self::borrowed::{AttributeView, ObjectView};
pub use self::owned::Attribute;

mod borrowed;
mod common;
#[allow(clippy::module_name_repetitions)]
pub mod error;
mod owned;
