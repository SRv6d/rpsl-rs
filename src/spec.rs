use std::convert::Infallible;

pub trait Specification {
    type NameError;
    type ValueError;

    fn validate_name(name: &str) -> Result<(), Self::NameError>;
    fn validate_value(value: &str) -> Result<(), Self::ValueError>;

}

pub struct Raw;

impl Specification for Raw{
    type NameError = Infallible;
    type ValueError = Infallible;

    fn validate_name(name: &str) -> Result<(), Self::NameError> {
        Ok(())
    }

    fn validate_value(value: &str) -> Result<(), Self::ValueError> {
        Ok(())
    }
}
