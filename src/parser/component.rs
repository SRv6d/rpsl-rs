use crate::Attribute;
use winnow::{
    ascii::{newline, space0},
    combinator::{delimited, separated_pair, terminated},
    token::take_while,
    PResult, Parser,
};

// A response code or message sent by the whois server.
// Starts with the "%" character and extends until the end of the line.
// In contrast to RPSL, characters are not limited to ASCII.
pub fn server_message<'s>(input: &mut &'s str) -> PResult<&'s str> {
    delimited(
        ('%', space0),
        take_while(1.., |c: char| !c.is_control()),
        newline,
    )
    .parse_next(input)
}

// A RPSL attribute consisting of a name and one or more values.
// The name is followed by a colon and optional spaces.
// Single value attributes are limited to one line, while multi value attributes span over multiple lines.
pub fn attribute<'s>(input: &mut &'s str) -> PResult<Attribute<'s>> {
    let (name, first_value) = separated_pair(
        terminated(subcomponent::attribute_name, ':'),
        space0,
        terminated(subcomponent::attribute_value, newline),
    )
    .parse_next(input)?;

    Ok(Attribute::unchecked_single(name, first_value))
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::*;

    #[rstest]
    #[case(
        &mut "% Note: this output has been filtered.\n",
        "Note: this output has been filtered.",
        ""
    )]
    #[case(
        &mut "%       To receive output for a database update, use the \"-B\" flag.\n",
        "To receive output for a database update, use the \"-B\" flag.",
        ""
    )]
    #[case(
        &mut "% This query was served by the RIPE Database Query Service version 1.106.1 (BUSA)\n",
        "This query was served by the RIPE Database Query Service version 1.106.1 (BUSA)",
        ""
    )]
    fn server_message_valid(
        #[case] given: &mut &str,
        #[case] expected: &str,
        #[case] remaining: &str,
    ) {
        let parsed = server_message(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    #[rstest]
    #[case(
        &mut "import:         from AS12 accept AS12\n",
        Attribute::unchecked_single("import", "from AS12 accept AS12"),
        ""
    )]
    fn attribute_valid_single_value(
        #[case] given: &mut &str,
        #[case] expected: Attribute,
        #[case] remaining: &str,
    ) {
        let parsed = attribute(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }

    #[rstest]
    #[case(
        &mut concat!(
            "remarks:        Locations\n",
            "                LA1 - CoreSite One Wilshire\n",
            "                NY1 - Equinix New York, Newark\n",
            "remarks:        Peering Policy\n",
        ),
        Attribute::unchecked_multi(
            "remarks",
            vec![
                "Locations",
                "LA1 - CoreSite One Wilshire",
                "NY1 - Equinix New York, Newark",
            ]
        ),
        "remarks:        Peering Policy\n"
    )]
    fn attribute_valid_multi_value(
        #[case] given: &mut &str,
        #[case] expected: Attribute,
        #[case] remaining: &str,
    ) {
        let parsed = attribute(given).unwrap();
        assert_eq!(parsed, expected);
        assert_eq!(*given, remaining);
    }
}

mod subcomponent {
    use winnow::{
        ascii::{newline, space0},
        combinator::{delimited, preceded},
        token::{one_of, take_while},
        PResult, Parser,
    };

    // An ASCII sequence of letters, digits and the characters "-", "_".
    // The first character must be a letter, while the last character may be a letter or a digit.
    pub fn attribute_name<'s>(input: &mut &'s str) -> PResult<&'s str> {
        take_while(2.., |c: char| {
            c.is_ascii_alphanumeric() || c == '-' || c == '_'
        })
        .verify(|s: &str| {
            s.starts_with(|c: char| c.is_ascii_alphabetic())
                && s.ends_with(|c: char| c.is_ascii_alphanumeric())
        })
        .parse_next(input)
    }

    // An ASCII sequence of characters, excluding control.
    pub fn attribute_value<'s>(input: &mut &'s str) -> PResult<&'s str> {
        take_while(1.., |c: char| c.is_ascii() && !c.is_ascii_control()).parse_next(input)
    }

    // Match and discard a single multiline continuation character.
    pub fn continuation_char(input: &mut &str) -> PResult<()> {
        one_of([' ', '\t', '+']).void().parse_next(input)
    }

    // Extends an attributes value over multiple lines.
    // Must start with a space, tab or a plus character.
    pub fn continuation_line<'s>(input: &mut &'s str) -> PResult<&'s str> {
        delimited(
            continuation_char,
            preceded(space0, attribute_value),
            newline,
        )
        .parse_next(input)
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use rstest::*;

        #[rstest]
        #[case(&mut "remarks:", "remarks", ":")]
        #[case(&mut "aut-num:", "aut-num", ":")]
        #[case(&mut "ASNumber:", "ASNumber", ":")]
        #[case(&mut "route6:", "route6", ":")]
        fn attribute_name_valid(
            #[case] given: &mut &str,
            #[case] expected: &str,
            #[case] remaining: &str,
        ) {
            let parsed = attribute_name(given).unwrap();
            assert_eq!(parsed, expected);
            assert_eq!(*given, remaining);
        }

        #[rstest]
        #[case(&mut "1remarks:")]
        #[case(&mut "-remarks:")]
        #[case(&mut "_remarks:")]
        fn attribute_name_non_letter_first_char_is_error(#[case] given: &mut &str) {
            assert!(attribute_name(given).is_err());
        }

        #[rstest]
        #[case(&mut "remarks-:")]
        #[case(&mut "remarks_:")]
        fn attribute_name_non_letter_or_digit_last_char_is_error(#[case] given: &mut &str) {
            assert!(attribute_name(given).is_err());
        }

        #[rstest]
        #[case(
            &mut "This is an example remark\n",
            "This is an example remark",
            "\n"
        )]
        #[case(
            &mut "Concerning abuse and spam ... mailto: abuse@asn.net\n",
            "Concerning abuse and spam ... mailto: abuse@asn.net",
            "\n"
        )]
        #[case(
            &mut "+49 176 07071964\n",
            "+49 176 07071964",
            "\n"
        )]
        #[case(
            &mut "* Equinix FR5, Kleyerstr, Frankfurt am Main\n",
            "* Equinix FR5, Kleyerstr, Frankfurt am Main",
            "\n"
        )]
        fn attribute_value_valid(
            #[case] given: &mut &str,
            #[case] expected: &str,
            #[case] remaining: &str,
        ) {
            let parsed = attribute_value(given).unwrap();
            assert_eq!(parsed, expected);
            assert_eq!(*given, remaining);
        }

        #[rstest]
        #[case(
            &mut "    continuation value prefixed by a space\n",
            "continuation value prefixed by a space",
            ""
        )]
        #[case(
            &mut "\t    continuation value prefixed by a tab\n",
            "continuation value prefixed by a tab",
            ""
        )]
        #[case(
            &mut "+    continuation value prefixed by a plus\n",
            "continuation value prefixed by a plus",
            ""
        )]
        fn continuation_line_valid(
            #[case] given: &mut &str,
            #[case] expected: &str,
            #[case] remaining: &str,
        ) {
            let parsed = continuation_line(given).unwrap();
            assert_eq!(parsed, expected);
            assert_eq!(*given, remaining);
        }
    }
}
