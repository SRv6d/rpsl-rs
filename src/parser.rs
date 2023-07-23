use nom::{
    bytes::complete::{tag, take_while, take_while1},
    character::complete::space0,
    IResult,
};

// An attributes name. A ASCII sequence of letters, digits and the characters "-", "_".
// The first character must be a letter, while the last character may be a letter or a digit.
fn rpsl_attribute_name(input: &str) -> IResult<&str, &str> {
    let (remaining, name) =
        take_while1(|c: char| c.is_ascii_alphanumeric() || c == '-' || c == '_')(input)?;
    Ok((remaining, name))
}

// An attributes value. A ASCII sequence of characters, excluding control.
fn rpsl_attribute_value(input: &str) -> IResult<&str, &str> {
    let (remaining, value) = take_while(|c: char| c.is_ascii() && !c.is_ascii_control())(input)?;
    Ok((remaining, value))
}

fn parse_attribute(input: &str) -> IResult<&str, (&str, &str)> {
    let (remaining, name) = rpsl_attribute_name(input)?;

    let (remaining, _) = tag(":")(remaining)?;
    let (remaining, _) = space0(remaining)?;

    let (remaining, value) = rpsl_attribute_value(remaining)?;
    let (remaining, _) = tag("\n")(remaining)?;

    Ok((remaining, (name, value)))
}

#[cfg(test)]
mod tests {
    use crate::parser::{parse_attribute, rpsl_attribute_name, rpsl_attribute_value};

    #[test]
    fn rpsl_attribute_name_test() {
        assert_eq!(rpsl_attribute_name("remarks:"), Ok((":", "remarks")));
        assert_eq!(rpsl_attribute_name("aut-num:"), Ok((":", "aut-num")));
        assert_eq!(rpsl_attribute_name("ASNumber:"), Ok((":", "ASNumber")));
        assert_eq!(rpsl_attribute_name("route6:"), Ok((":", "route6")));
    }

    #[test]
    fn rpsl_attribute_value_test() {
        assert_eq!(
            rpsl_attribute_value("This is an example remark\n"),
            Ok(("\n", "This is an example remark"))
        );
        assert_eq!(
            rpsl_attribute_value("Concerning abuse and spam ... mailto: abuse@asn.net\n"),
            Ok(("\n", "Concerning abuse and spam ... mailto: abuse@asn.net"))
        );
        assert_eq!(
            rpsl_attribute_value("+49 176 07071964\n"),
            Ok(("\n", "+49 176 07071964"))
        );
        assert_eq!(
            rpsl_attribute_value("* Equinix FR5, Kleyerstr, Frankfurt am Main\n"),
            Ok(("\n", "* Equinix FR5, Kleyerstr, Frankfurt am Main"))
        );
    }

    #[test]
    fn parse_attribute_test() {
        assert_eq!(
            parse_attribute("import:         from AS12 accept AS12\n"),
            Ok(("", ("import", "from AS12 accept AS12")))
        );
    }
}
