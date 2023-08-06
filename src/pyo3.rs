use super::parser;
use pyo3::prelude::*;

type PyRPSLAtrribute = (String, Vec<Option<String>>);
type PyRPSLObject = Vec<PyRPSLAtrribute>;

pyo3::create_exception!(rpsl_parser, RPSLParseError, pyo3::exceptions::PyException);

#[pyfunction]
fn parse_rpsl_object(rpsl: &str, _py: Python) -> PyResult<PyObject> {
    match parser::parse_rpsl_object(rpsl) {
        Err(_) => Err(RPSLParseError::new_err("Failed to parse RPSL object.")),
        Ok(parsed) => {
            let object: PyRPSLObject = parsed
                .into_iter()
                .map(|attribute| (attribute.name, attribute.values))
                .collect();

            Ok(object.into_py(_py))
        }
    }
}

#[pymodule]
fn rpsl_parser(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add("RPSLParseError", _py.get_type::<RPSLParseError>())?;
    m.add_function(wrap_pyfunction!(parse_rpsl_object, m)?)?;
    Ok(())
}
