use rpsl_parser::parse_rpsl_object;
use std::{env, fs};

fn main() {
    let rpsl_filepath = env::args().nth(1).expect("No RPSL file provided");
    let rpsl = fs::read_to_string(rpsl_filepath).expect("Unable to read file");
    parse_rpsl_object(&rpsl);
}
