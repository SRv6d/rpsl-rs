pub use self::attribute::Attribute;
pub use self::error::AttributeError;
pub use self::object::Object;

mod attribute;
#[allow(clippy::module_name_repetitions)]
mod error;
mod object;
