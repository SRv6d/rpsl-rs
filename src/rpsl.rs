pub use self::borrowed::{AttributeView, ObjectView};

mod borrowed;
mod common;
#[allow(clippy::module_name_repetitions)]
pub mod error;
mod owned;
