use crate::rpsl::Attribute;
use nom::{
    bytes::complete::{tag, take_while},
    character::complete::{newline, space0},
    combinator::peek,
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
        newline,
    )(input)?;

    Ok((remaining, value))
}

// A RPSL attribute consisting of a name and one or more values.
// The name is followed by a colon and optional spaces.
// Single value attributes are limited to one line, while multi value attributes span over multiple lines.
pub fn attribute(input: &str) -> IResult<&str, Attribute> {
    let (remaining, (name, first_value)) = separated_pair(
        terminated(subcomponent::attribute_name, tag(":")),
        space0,
        terminated(subcomponent::attribute_value, newline),
    )(input)?;

    match peek(subcomponent::continuation_char)(remaining) {
        Err(_) => Ok((remaining, Attribute::new(name, first_value))),
        Ok(_) => {
            let (remaining, continuation_values) =
                many0(subcomponent::continuation_line)(remaining)?;
            let mut values: Vec<&str> = Vec::with_capacity(1 + continuation_values.len());
            values.push(first_value);
            values.extend(continuation_values);
            Ok((remaining, Attribute::new(name, values)))
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    mod server_message {
        use super::*;

        #[test]
        fn valid() {
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
    }

    mod attribute {
        use super::*;

        #[test]
        fn valid_single_value() {
            assert_eq!(
                attribute("import:         from AS12 accept AS12\n"),
                Ok(("", Attribute::new("import", "from AS12 accept AS12")))
            );
        }

        #[test]
        fn valid_multi_value() {
            assert_eq!(
                attribute(concat!(
                    "remarks:        Locations\n",
                    "                LA1 - CoreSite One Wilshire\n",
                    "                NY1 - Equinix New York, Newark\n",
                    "remarks:        Peering Policy\n",
                )),
                Ok((
                    "remarks:        Peering Policy\n",
                    Attribute::new(
                        "remarks",
                        vec![
                            "Locations",
                            "LA1 - CoreSite One Wilshire",
                            "NY1 - Equinix New York, Newark",
                        ]
                    )
                ))
            );
        }
    }
}

mod subcomponent {
    use nom::{
        bytes::complete::{take_while, take_while1},
        character::complete::{newline, one_of, space0},
        combinator::verify,
        sequence::{delimited, preceded},
        IResult,
    };

    // An ASCII sequence of letters, digits and the characters "-", "_".
    // The first character must be a letter, while the last character may be a letter or a digit.
    pub fn attribute_name(input: &str) -> IResult<&str, &str> {
        let (remaining, name) = verify(
            take_while1(|c: char| c.is_ascii_alphanumeric() || c == '-' || c == '_'),
            |s: &str| {
                s.chars().next().unwrap().is_ascii_alphabetic()
                    && s.chars().last().unwrap().is_ascii_alphanumeric()
            },
        )(input)?;
        Ok((remaining, name))
    }

    // An ASCII sequence of characters, excluding control.
    pub fn attribute_value(input: &str) -> IResult<&str, &str> {
        let (remaining, value) =
            take_while(|c: char| c.is_ascii() && !c.is_ascii_control())(input)?;
        Ok((remaining, value))
    }

    // A single multiline continuation character.
    pub fn continuation_char(input: &str) -> IResult<&str, char> {
        let (remaining, char) = one_of(" \t+")(input)?;
        Ok((remaining, char))
    }

    // Extends an attributes value over multiple lines.
    // Must start with a space, tab or a plus character.
    pub fn continuation_line(input: &str) -> IResult<&str, &str> {
        let (remaining, value) = delimited(
            continuation_char,
            preceded(space0, attribute_value),
            newline,
        )(input)?;

        Ok((remaining, value))
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        mod attribute_name {
            use super::*;

            #[test]
            fn valid() {
                assert_eq!(attribute_name("remarks:"), Ok((":", "remarks")));
                assert_eq!(attribute_name("aut-num:"), Ok((":", "aut-num")));
                assert_eq!(attribute_name("ASNumber:"), Ok((":", "ASNumber")));
                assert_eq!(attribute_name("route6:"), Ok((":", "route6")));
            }

            #[test]
            fn non_letter_first_char_is_error() {
                assert!(attribute_name("1remarks:").is_err());
                assert!(attribute_name("-remarks:").is_err());
                assert!(attribute_name("_remarks:").is_err());
            }

            #[test]
            fn non_letter_or_digit_last_char_is_error() {
                assert!(attribute_name("remarks-:").is_err());
                assert!(attribute_name("remarks_:").is_err());
            }
        }

        mod attribute_value {
            use super::*;

            #[test]
            fn valid() {
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
        }

        mod continuation_line {
            use super::*;

            #[test]
            fn valid() {
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
}
