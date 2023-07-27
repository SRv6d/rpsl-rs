use nom::{
    bytes::complete::{tag, take_while, take_while1},
    character::complete::{one_of, space0},
    multi::many0,
    sequence::{delimited, separated_pair, terminated, tuple},
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

// A continuation line. Extends an attributes value over multiple lines.
// Must start with a space, tab or a plus character.
fn rpsl_continuation_line(input: &str) -> IResult<&str, &str> {
    let continuation_char = one_of(" \t+");
    let (remaining, (_, _, value, _)) =
        tuple((continuation_char, space0, rpsl_attribute_value, tag("\n")))(input)?;

    Ok((remaining, value))
}

// An info line sent by the whois server. Starts with the "%" character and extends until the end of the line.
// The value may be prefixed by whitespace and contain any unicode character excluding control characters.
fn server_info_line(input: &str) -> IResult<&str, &str> {
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
fn rpsl_attribute(input: &str) -> IResult<&str, (&str, Vec<&str>)> {
    let (remaining, (name, first_value)) = separated_pair(
        terminated(rpsl_attribute_name, tag(":")),
        space0,
        terminated(rpsl_attribute_value, tag("\n")),
    )(input)?;
    let (remaining, continuation_values) = many0(rpsl_continuation_line)(remaining)?;

    let mut values: Vec<&str> = Vec::with_capacity(1 + continuation_values.len());
    values.push(first_value);
    values.extend(continuation_values);

    Ok((remaining, (name, values)))
}

#[cfg(test)]
mod tests {
    use super::*;

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
    fn rpsl_continuation_line_test() {
        assert_eq!(
            rpsl_continuation_line("    continuation value prefixed by a space\n"),
            Ok(("", "continuation value prefixed by a space"))
        );
        assert_eq!(
            rpsl_continuation_line("\t    continuation value prefixed by a tab\n"),
            Ok(("", "continuation value prefixed by a tab"))
        );
        assert_eq!(
            rpsl_continuation_line("+    continuation value prefixed by a plus\n"),
            Ok(("", "continuation value prefixed by a plus"))
        );
    }

    #[test]
    fn server_info_line_test() {
        assert_eq!(
            server_info_line("% Note: this output has been filtered.\n"),
            Ok(("", "Note: this output has been filtered."))
        );
        assert_eq!(
            server_info_line(
                "%       To receive output for a database update, use the \"-B\" flag.\n"
            ),
            Ok((
                "",
                "To receive output for a database update, use the \"-B\" flag."
            ))
        );
        assert_eq!(
            server_info_line(
                "% This query was served by the RIPE Database Query Service version 1.106.1 (BUSA)\n"
            ),
            Ok((
                "",
                "This query was served by the RIPE Database Query Service version 1.106.1 (BUSA)"
            ))
        );
    }

    #[test]
    fn single_value_rpsl_attribute_test() {
        assert_eq!(
            rpsl_attribute("import:         from AS12 accept AS12\n"),
            Ok(("", ("import", vec!["from AS12 accept AS12"])))
        )
    }

    #[test]
    fn multi_value_rpsl_attribute_test() {
        assert_eq!(
            rpsl_attribute(concat!(
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

    #[test]
    fn parse_rpsl_with_multiple_objects() {
        let rpsl = concat!(
            "as-block:       AS12557 - AS13223\n",
            "descr:          RIPE NCC ASN block\n",
            "remarks:        These AS Numbers are assigned to network operators in the RIPE NCC service region.\n",
            "mnt-by:         RIPE-NCC-HM-MNT\n",
            "created:        2018-11-22T15:27:24Z\n",
            "last-modified:  2018-11-22T15:27:24Z\n",
            "source:         RIPE\n",
            "\n",
            "% Information related to 'AS13030\n",
            "\n",
            "% Abuse contact for 'AS13030' is 'abuse@init7.net'\n",
            "\n",
            "aut-num:        AS13030\n",
            "as-name:        INIT7\n",
            "org:            ORG-ISA1-RIPE\n",
            "remarks:        Init7 Global Backbone\n",
            "\n",
            "organisation:   ORG-ISA1-RIPE\n",
            "org-name:       Init7 (Switzerland) Ltd.\n",
            "\n"
        );
        let expected: Vec<Vec<(&str, Vec<&str>)>> = vec![
            vec![
                ("as-block", vec!["AS12557 - AS13223"]),
                ("descr", vec!["RIPE NCC ASN block"]),
                (
                    "remarks",
                    vec![
                        "These AS Numbers are assigned to network operators in the RIPE NCC service region."
                    ]
                ),
                ("mnt-by", vec!["RIPE-NCC-HM-MNT"]),
                ("created", vec!["2018-11-22T15:27:24Z"]),
                ("last-modified", vec!["2018-11-22T15:27:24Z"]),
                ("source", vec!["RIPE"]),
            ],
            vec![
                ("aut-num", vec!["AS13030"]),
                ("as-name", vec!["INIT7"]),
                ("org", vec!["ORG-ISA1-RIPE"]),
                ("remarks", vec!["Init7 Global Backbone"]),
            ],
            vec![
                ("organisation", vec!["ORG-ISA1-RIPE"]),
                ("org-name", vec!["Init7 (Switzerland) Ltd."]),
            ],
        ];

        assert_eq!(parse_rpsl(rpsl), expected);
    }
}
