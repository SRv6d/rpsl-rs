use super::parser;
use pyo3::{prelude::*, types::PyTuple};

pyo3::create_exception!(rpsl_parser, RPSLParseError, pyo3::exceptions::PyException);

#[pyfunction]
fn parse_rpsl_object<'a>(rpsl: &'a str, py: Python<'a>) -> PyResult<&'a PyTuple> {
    match parser::parse_rpsl_object(rpsl) {
        Err(_) => Err(RPSLParseError::new_err("Failed to parse RPSL object.")),
        Ok(parsed) => Ok(PyTuple::new(
            py,
            parsed
                .into_iter()
                .map(|attribute| (attribute.name, PyTuple::new(py, attribute.values))),
        )),
    }
}

#[pymodule]
fn rpsl_parser(py: Python, m: &PyModule) -> PyResult<()> {
    m.add("RPSLParseError", py.get_type::<RPSLParseError>())?;
    m.add_function(wrap_pyfunction!(parse_rpsl_object, m)?)?;
    Ok(())
}
