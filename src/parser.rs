mod component {

    use nom::{
        bytes::complete::{tag, take_while, take_while1},
        character::complete::{one_of, space0},
        multi::many0,
        sequence::{delimited, separated_pair, terminated, tuple},
        IResult,
    };

    mod subcomponent {
        use super::*;

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
            )
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
}

use super::rpsl::{RpslObject, RpslObjectCollection};
use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::multispace0,
    combinator::all_consuming,
    multi::{many0, many1},
    sequence::{delimited, preceded, terminated},
};

/// Parse a string containing an RPSL object into a vector of it's attributes.
pub fn parse_rpsl_object(rpsl: &str) -> RpslObject {
    let (_, object) = all_consuming(delimited(
        multispace0,
        many1(component::attribute),
        multispace0,
    ))(rpsl)
    .unwrap();
    RpslObject::from(object)
}

/// Parse a string containing a whois server response into a vector of RPSL objects.
pub fn parse_rpsl_server_response(response: &str) -> RpslObjectCollection {
    let rpsl_object = many1(component::attribute);
    let empty_or_server_message = alt((component::server_message, tag("\n")));

    let (_, objects) = all_consuming(terminated(
        many1(preceded(many0(empty_or_server_message), rpsl_object)),
        tag("\n"),
    ))(response)
    .unwrap();

    RpslObjectCollection::from(objects)
}

#[cfg(test)]
mod tests {
    use super::*;

    use crate::rpsl::RpslAttribute;

    #[test]
    fn parse_valid_rpsl_object() {
        let rpsl = concat!(
            "\n",
            "role:           Twelve99 Routing Registry\n",
            "remarks:\n",
            "remarks:        This is a remark.\n",
            "address:        Arelion Sweden AB\n",
            "address:        Evenemangsgatan 2C\n",
            "address:        SE-169 79 SOLNA\n",
            "address:        Sweden\n",
            "e-mail:         routing-registry@99.net\n",
            "nic-hdl:        TRR2-RIPE\n",
            "notify:         routing-registry@99.net\n",
            "mnt-by:         Twelve99-IRR-MNT\n",
            "created:        2002-05-27T15:05:16Z\n",
            "last-modified:  2023-01-30T11:49:56Z\n",
            "source:         RIPE\n",
            "\n",
            "\n",
        );
        let expected = RpslObject::new(vec![
            RpslAttribute::new(
                "role".to_string(),
                vec![Some("Twelve99 Routing Registry".to_string())],
            ),
            RpslAttribute::new("remarks".to_string(), vec![None]),
            RpslAttribute::new(
                "remarks".to_string(),
                vec![Some("This is a remark.".to_string())],
            ),
            RpslAttribute::new(
                "address".to_string(),
                vec![Some("Arelion Sweden AB".to_string())],
            ),
            RpslAttribute::new(
                "address".to_string(),
                vec![Some("Evenemangsgatan 2C".to_string())],
            ),
            RpslAttribute::new(
                "address".to_string(),
                vec![Some("SE-169 79 SOLNA".to_string())],
            ),
            RpslAttribute::new("address".to_string(), vec![Some("Sweden".to_string())]),
            RpslAttribute::new(
                "e-mail".to_string(),
                vec![Some("routing-registry@99.net".to_string())],
            ),
            RpslAttribute::new("nic-hdl".to_string(), vec![Some("TRR2-RIPE".to_string())]),
            RpslAttribute::new(
                "notify".to_string(),
                vec![Some("routing-registry@99.net".to_string())],
            ),
            RpslAttribute::new(
                "mnt-by".to_string(),
                vec![Some("Twelve99-IRR-MNT".to_string())],
            ),
            RpslAttribute::new(
                "created".to_string(),
                vec![Some("2002-05-27T15:05:16Z".to_string())],
            ),
            RpslAttribute::new(
                "last-modified".to_string(),
                vec![Some("2023-01-30T11:49:56Z".to_string())],
            ),
            RpslAttribute::new("source".to_string(), vec![Some("RIPE".to_string())]),
        ]);

        assert_eq!(parse_rpsl_object(rpsl), expected);
    }

    #[test]
    fn parse_valid_server_response() {
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
        let expected = RpslObjectCollection::new(vec![
            RpslObject::new(vec![
                RpslAttribute::new(
                    "as-block".to_string(),
                    vec![Some("AS12557 - AS13223".to_string())],
                ),
                RpslAttribute::new(
                    "descr".to_string(),
                    vec![Some("RIPE NCC ASN block".to_string())],
                ),
                RpslAttribute::new(
                    "remarks".to_string(),
                    vec![Some(
                        "These AS Numbers are assigned to network operators in the RIPE NCC service region.".to_string(),
                    )],
                ),
                RpslAttribute::new(
                    "mnt-by".to_string(),
                    vec![Some("RIPE-NCC-HM-MNT".to_string())],
                ),
                RpslAttribute::new(
                    "created".to_string(),
                    vec![Some("2018-11-22T15:27:24Z".to_string())],
                ),
                RpslAttribute::new(
                    "last-modified".to_string(),
                    vec![Some("2018-11-22T15:27:24Z".to_string())],
                ),
                RpslAttribute::new("source".to_string(), vec![Some("RIPE".to_string())]),
            ]),
            RpslObject::new(vec![
                RpslAttribute::new("aut-num".to_string(), vec![Some("AS13030".to_string())]),
                RpslAttribute::new("as-name".to_string(), vec![Some("INIT7".to_string())]),
                RpslAttribute::new("org".to_string(), vec![Some("ORG-ISA1-RIPE".to_string())]),
                RpslAttribute::new(
                    "remarks".to_string(),
                    vec![Some("Init7 Global Backbone".to_string())],
                ),
            ]),
            RpslObject::new(vec![
                RpslAttribute::new(
                    "organisation".to_string(),
                    vec![Some("ORG-ISA1-RIPE".to_string())],
                ),
                RpslAttribute::new(
                    "org-name".to_string(),
                    vec![Some("Init7 (Switzerland) Ltd.".to_string())],
                ),
            ]),
        ]);

        assert_eq!(parse_rpsl_server_response(rpsl), expected);
    }
}
