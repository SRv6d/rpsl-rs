use crate::AttributeView;
use nom::{
    bytes::complete::{tag, take_while},
    character::complete::{newline, space0},
    combinator::peek,
    multi::many0,
    sequence::{delimited, separated_pair, terminated, tuple},
    IResult,
};
use winnow::{PResult, Parser};

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

// A response code or message sent by the whois server.
// Starts with the "%" character and extends until the end of the line.
// In contrast to RPSL, characters are not limited to ASCII.
pub fn w_server_message<'s>(input: &mut &'s str) -> PResult<&'s str> {
    winnow::combinator::delimited(
        ('%', winnow::ascii::space0),
        winnow::token::take_while(1.., |c: char| !c.is_control()),
        winnow::ascii::newline,
    )
    .parse_next(input)
}

// A RPSL attribute consisting of a name and one or more values.
// The name is followed by a colon and optional spaces.
// Single value attributes are limited to one line, while multi value attributes span over multiple lines.
pub fn attribute(input: &str) -> IResult<&str, AttributeView> {
    let (remaining, (name, first_value)) = separated_pair(
        terminated(subcomponent::attribute_name, tag(":")),
        space0,
        terminated(subcomponent::attribute_value, newline),
    )(input)?;

    if peek(subcomponent::continuation_char)(remaining).is_err() {
        Ok((remaining, AttributeView::new_single(name, first_value)))
    } else {
        let (remaining, continuation_values) = many0(subcomponent::continuation_line)(remaining)?;
        let values = std::iter::once(first_value)
            .chain(continuation_values)
            .collect();
        Ok((remaining, AttributeView::new_multi(name, values)))
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::*;

    #[test]
    fn server_message_valid() {
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

    #[rstest]
    #[case(&mut "% Note: this output has been filtered.\n", "Note: this output has been filtered.", "")]
    #[case(&mut "%       To receive output for a database update, use the \"-B\" flag.\n", "To receive output for a database update, use the \"-B\" flag.", "")]
    #[case(&mut "% This query was served by the RIPE Database Query Service version 1.106.1 (BUSA)\n", "This query was served by the RIPE Database Query Service version 1.106.1 (BUSA)", "")]
    fn w_server_message_valid(
        #[case] given: &mut &str,
        #[case] expected: &str,
        #[case] remaining: &str,
    ) {
        let parsed = w_server_message(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    #[test]
    fn attribute_valid_single_value() {
        assert_eq!(
            attribute("import:         from AS12 accept AS12\n"),
            Ok((
                "",
                AttributeView::new_single("import", "from AS12 accept AS12")
            ))
        );
    }

    #[test]
    fn attribute_valid_multi_value() {
        assert_eq!(
            attribute(concat!(
                "remarks:        Locations\n",
                "                LA1 - CoreSite One Wilshire\n",
                "                NY1 - Equinix New York, Newark\n",
                "remarks:        Peering Policy\n",
            )),
            Ok((
                "remarks:        Peering Policy\n",
                AttributeView::new_multi(
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

mod subcomponent {
    use nom::{
        bytes::complete::{take_while, take_while1},
        character::complete::{newline, one_of, space0},
        combinator::verify,
        sequence::{delimited, preceded},
        IResult,
    };
    use winnow::{PResult, Parser};

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

    // An ASCII sequence of letters, digits and the characters "-", "_".
    // The first character must be a letter, while the last character may be a letter or a digit.
    pub fn w_attribute_name<'s>(input: &mut &'s str) -> PResult<&'s str> {
        winnow::token::take_while(2.., |c: char| {
            c.is_ascii_alphanumeric() || c == '-' || c == '_'
        })
        .verify(|s: &str| {
            s.starts_with(|c: char| c.is_ascii_alphabetic())
                && s.ends_with(|c: char| c.is_ascii_alphanumeric())
        })
        .parse_next(input)
    }

    // An ASCII sequence of characters, excluding control.
    pub fn attribute_value(input: &str) -> IResult<&str, &str> {
        let (remaining, value) =
            take_while(|c: char| c.is_ascii() && !c.is_ascii_control())(input)?;
        Ok((remaining, value))
    }

    // An ASCII sequence of characters, excluding control.
    pub fn w_attribute_value<'s>(input: &mut &'s str) -> PResult<&'s str> {
        winnow::token::take_while(1.., |c: char| c.is_ascii() && !c.is_ascii_control())
            .parse_next(input)
    }

    // A single multiline continuation character.
    pub fn continuation_char(input: &str) -> IResult<&str, char> {
        let (remaining, char) = one_of(" \t+")(input)?;
        Ok((remaining, char))
    }

    // Match and discard a single multiline continuation character.
    pub fn w_continuation_char(input: &mut &str) -> PResult<()> {
        winnow::token::one_of([' ', '\t', '+'])
            .void()
            .parse_next(input)
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

    // Extends an attributes value over multiple lines.
    // Must start with a space, tab or a plus character.
    pub fn w_continuation_line<'s>(input: &mut &'s str) -> PResult<&'s str> {
        winnow::combinator::delimited(
            w_continuation_char,
            winnow::combinator::preceded(winnow::ascii::space0, w_attribute_value),
            winnow::ascii::newline,
        )
        .parse_next(input)
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use rstest::*;

        #[test]
        fn attribute_name_valid() {
            assert_eq!(attribute_name("remarks:"), Ok((":", "remarks")));
            assert_eq!(attribute_name("aut-num:"), Ok((":", "aut-num")));
            assert_eq!(attribute_name("ASNumber:"), Ok((":", "ASNumber")));
            assert_eq!(attribute_name("route6:"), Ok((":", "route6")));
        }

        #[rstest]
        #[case(&mut "remarks:", "remarks", ":")]
        #[case(&mut "aut-num:", "aut-num", ":")]
        #[case(&mut "ASNumber:", "ASNumber", ":")]
        #[case(&mut "route6:", "route6", ":")]
        fn w_attribute_name_valid(
            #[case] given: &mut &str,
            #[case] expected: &str,
            #[case] remaining: &str,
        ) {
            let parsed = w_attribute_name(given).unwrap();
            assert_eq!(parsed, expected);
            assert_eq!(*given, remaining);
        }

        #[test]
        fn attribute_name_non_letter_first_char_is_error() {
            assert!(attribute_name("1remarks:").is_err());
            assert!(attribute_name("-remarks:").is_err());
            assert!(attribute_name("_remarks:").is_err());
        }

        #[rstest]
        #[case(&mut "1remarks:")]
        #[case(&mut "-remarks:")]
        #[case(&mut "_remarks:")]
        fn w_attribute_name_non_letter_first_char_is_error(#[case] given: &mut &str) {
            assert!(w_attribute_name(given).is_err());
        }

        #[test]
        fn attribute_name_non_letter_or_digit_last_char_is_error() {
            assert!(attribute_name("remarks-:").is_err());
            assert!(attribute_name("remarks_:").is_err());
        }

        #[rstest]
        #[case(&mut "remarks-:")]
        #[case(&mut "remarks_:")]
        fn w_attribute_name_non_letter_or_digit_last_char_is_error(#[case] given: &mut &str) {
            assert!(w_attribute_name(given).is_err());
        }

        #[test]
        fn attribute_value_valid() {
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

        #[rstest]
        #[case(&mut "This is an example remark\n", "This is an example remark", "\n")]
        #[case(&mut "Concerning abuse and spam ... mailto: abuse@asn.net\n", "Concerning abuse and spam ... mailto: abuse@asn.net", "\n")]
        #[case(&mut "+49 176 07071964\n", "+49 176 07071964", "\n")]
        #[case(&mut "* Equinix FR5, Kleyerstr, Frankfurt am Main\n", "* Equinix FR5, Kleyerstr, Frankfurt am Main", "\n")]
        fn w_attribute_value_valid(
            #[case] given: &mut &str,
            #[case] expected: &str,
            #[case] remaining: &str,
        ) {
            let parsed = w_attribute_value(given).unwrap();
            assert_eq!(parsed, expected);
            assert_eq!(*given, remaining);
        }

        #[test]
        fn continuation_line_valid() {
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

        #[rstest]
        #[case(&mut "    continuation value prefixed by a space\n", "continuation value prefixed by a space", "")]
        #[case(&mut "\t    continuation value prefixed by a tab\n", "continuation value prefixed by a tab", "")]
        #[case(&mut "+    continuation value prefixed by a plus\n", "continuation value prefixed by a plus", "")]
        fn w_continuation_line_valid(
            #[case] given: &mut &str,
            #[case] expected: &str,
            #[case] remaining: &str,
        ) {
            let parsed = w_continuation_line(given).unwrap();
            assert_eq!(parsed, expected);
            assert_eq!(*given, remaining);
        }
    }
}
