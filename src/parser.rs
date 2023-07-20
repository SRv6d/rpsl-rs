use nom::{
    bytes::complete::{tag, take_until, take_while},
    character::complete::space0,
    IResult,
};

fn attribute_name(input: &str) -> IResult<&str, &str> {
    let (remaining, name) = take_while(|c: char| c.is_alphanumeric() || c == '-')(input)?;
    let (remaining, _) = tag(":")(remaining)?;

    Ok((remaining, name))
}

fn attribute_value(input: &str) -> IResult<&str, &str> {
    let (remaining, _) = space0(input)?;
    let (remaining, value) = take_until("\n")(remaining)?;
    let (remaining, _) = tag("\n")(remaining)?;

    Ok((remaining, value))
}

#[cfg(test)]
mod tests {
    use crate::parser::{attribute_name, attribute_value};

    #[test]
    fn parse_attribute_name() {
        let input = "example-name:        example-value\n";

        let (rest, result) = attribute_name(input).unwrap();

        assert_eq!(rest, "        example-value\n");
        assert_eq!(result, "example-name");
    }

    #[test]
    fn parse_single_value() {
        let input = "        example-value\n";

        let (rest, result) = attribute_value(input).unwrap();

        assert_eq!(rest, "");
        assert_eq!(result, "example-value");
    }

    #[test]
    fn parse_multi_value() {
        let input = "        example-value\n                continuation-value\n";

        let (rest, result) = attribute_value(input).unwrap();

        assert_eq!(rest, "");
        assert_eq!(result, "example-value\n                continuation-value");
    }
}
