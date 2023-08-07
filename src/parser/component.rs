use nom::{
    bytes::complete::{tag, take_while, take_while1},
    character::complete::{one_of, space0},
    multi::many0,
    sequence::{delimited, separated_pair, terminated, tuple},
    IResult,
};

// A response code or message sent by the whois server.
// Starts with the "%" character and extends until the end of the line.
// In contrast to RPSL, characters are not limited to ASCII.
pub fn server_message(input: &str) -> IResult<&str, &str> {
    let (remaining, value) = delimited(
        tuple((tag("%"), space0)),
        take_while(|c: char| !c.is_control()),
        tag("\n"),
    )(input)?;

    Ok((remaining, value))
}

// A RPSL attribute consisting of a name and one or more values.
// The name is followed by a colon and optional spaces.
// Single value attributes are limited to one line, while multi value attributes span over multiple lines.
pub fn attribute(input: &str) -> IResult<&str, (&str, Vec<&str>)> {
    let (remaining, (name, first_value)) = separated_pair(
        terminated(subcomponent::attribute_name, tag(":")),
        space0,
        terminated(subcomponent::attribute_value, tag("\n")),
    )(input)?;
    let (remaining, continuation_values) = many0(subcomponent::continuation_line)(remaining)?;

    let mut values: Vec<&str> = Vec::with_capacity(1 + continuation_values.len());
    values.push(first_value);
    values.extend(continuation_values);

    Ok((remaining, (name, values)))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn valid_server_message() {
        assert_eq!(
            server_message("% Note: this output has been filtered.\n"),
            Ok(("", "Note: this output has been filtered."))
        );
        assert_eq!(
            server_message(
                "%       To receive output for a database update, use the \"-B\" flag.\n"
            ),
            Ok((
                "",
                "To receive output for a database update, use the \"-B\" flag."
            ))
        );
        assert_eq!(
            server_message(
                "% This query was served by the RIPE Database Query Service version 1.106.1 (BUSA)\n"
            ),
            Ok((
                "",
                "This query was served by the RIPE Database Query Service version 1.106.1 (BUSA)"
            ))
        );
    }

    #[test]
    fn valid_single_value_attribute() {
        assert_eq!(
            attribute("import:         from AS12 accept AS12\n"),
            Ok(("", ("import", vec!["from AS12 accept AS12"])))
        );
    }

    #[test]
    fn valid_multi_value_attribute_test() {
        assert_eq!(
            attribute(concat!(
                "remarks:        Locations\n",
                "                LA1 - CoreSite One Wilshire\n",
                "                NY1 - Equinix New York, Newark\n",
                "remarks:        Peering Policy\n",
            )),
            Ok((
                "remarks:        Peering Policy\n",
                (
                    "remarks",
                    vec![
                        "Locations",
                        "LA1 - CoreSite One Wilshire",
                        "NY1 - Equinix New York, Newark"
                    ]
                )
            ))
        );
    }
}

mod subcomponent {
    use super::{one_of, space0, tag, take_while, take_while1, tuple, IResult};

    // An ASCII sequence of letters, digits and the characters "-", "_".
    // The first character must be a letter, while the last character may be a letter or a digit.
    // TODO: ^ implement this invariant
    pub fn attribute_name(input: &str) -> IResult<&str, &str> {
        let (remaining, name) =
            take_while1(|c: char| c.is_ascii_alphanumeric() || c == '-' || c == '_')(input)?;
        Ok((remaining, name))
    }

    // An ASCII sequence of characters, excluding control.
    pub fn attribute_value(input: &str) -> IResult<&str, &str> {
        let (remaining, value) =
            take_while(|c: char| c.is_ascii() && !c.is_ascii_control())(input)?;
        Ok((remaining, value))
    }

    // Extends an attributes value over multiple lines.
    // Must start with a space, tab or a plus character.
    pub fn continuation_line(input: &str) -> IResult<&str, &str> {
        let continuation_char = one_of(" \t+");
        let (remaining, (_, _, value, _)) =
            tuple((continuation_char, space0, attribute_value, tag("\n")))(input)?;

        Ok((remaining, value))
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn valid_attribute_name() {
            assert_eq!(attribute_name("remarks:"), Ok((":", "remarks")));
            assert_eq!(attribute_name("aut-num:"), Ok((":", "aut-num")));
            assert_eq!(attribute_name("ASNumber:"), Ok((":", "ASNumber")));
            assert_eq!(attribute_name("route6:"), Ok((":", "route6")));
        }

        #[test]
        fn valid_attribute_value() {
            assert_eq!(
                attribute_value("This is an example remark\n"),
                Ok(("\n", "This is an example remark"))
            );
            assert_eq!(
                attribute_value("Concerning abuse and spam ... mailto: abuse@asn.net\n"),
                Ok(("\n", "Concerning abuse and spam ... mailto: abuse@asn.net"))
            );
            assert_eq!(
                attribute_value("+49 176 07071964\n"),
                Ok(("\n", "+49 176 07071964"))
            );
            assert_eq!(
                attribute_value("* Equinix FR5, Kleyerstr, Frankfurt am Main\n"),
                Ok(("\n", "* Equinix FR5, Kleyerstr, Frankfurt am Main"))
            );
        }

        #[test]
        fn valid_continuation_line() {
            assert_eq!(
                continuation_line("    continuation value prefixed by a space\n"),
                Ok(("", "continuation value prefixed by a space"))
            );
            assert_eq!(
                continuation_line("\t    continuation value prefixed by a tab\n"),
                Ok(("", "continuation value prefixed by a tab"))
            );
            assert_eq!(
                continuation_line("+    continuation value prefixed by a plus\n"),
                Ok(("", "continuation value prefixed by a plus"))
            );
        }
    }
}
