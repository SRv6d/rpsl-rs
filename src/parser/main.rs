use super::component;
use crate::rpsl;
use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::multispace0,
    combinator::all_consuming,
    error::Error,
    multi::{many0, many1},
    sequence::{delimited, preceded, terminated},
    Finish,
};

/// Parse a string containing a RPSL object.
///
/// # Errors
/// Returns nom `Error` if any error occurs during parsing.
///
/// # Examples
/// ```
/// use rpsl_parser::{parse_rpsl_object, rpsl};
/// let role_acme = "
/// role:        ACME Company
/// address:     Packet Street 6
/// address:     128 Series of Tubes
/// address:     Internet
/// email:       rpsl-parser@github.com
/// nic-hdl:     RPSL1-RIPE
/// source:      RIPE
/// ";
/// let parsed_attributes = parse_rpsl_object(role_acme).unwrap();
/// assert_eq!(
///     parsed_attributes,
///     rpsl::Object::new(vec![
///         rpsl::Attribute::new("role".to_string(), vec![Some("ACME Company".to_string())]),
///         rpsl::Attribute::new(
///             "address".to_string(),
///             vec![Some("Packet Street 6".to_string())],
///         ),
///         rpsl::Attribute::new(
///             "address".to_string(),
///             vec![Some("128 Series of Tubes".to_string())],
///         ),
///         rpsl::Attribute::new("address".to_string(), vec![Some("Internet".to_string())]),
///         rpsl::Attribute::new(
///             "email".to_string(),
///             vec![Some("rpsl-parser@github.com".to_string())],
///         ),
///         rpsl::Attribute::new("nic-hdl".to_string(), vec![Some("RPSL1-RIPE".to_string())]),
///         rpsl::Attribute::new("source".to_string(), vec![Some("RIPE".to_string())]),
///     ])
/// );
/// ```
pub fn parse_rpsl_object(rpsl: &str) -> Result<rpsl::Object, Error<&str>> {
    let (_, object) = all_consuming(delimited(
        multispace0,
        many1(component::attribute),
        multispace0,
    ))(rpsl)
    .finish()?;

    Ok(rpsl::Object::from(object))
}

/// Parse a string containing a whois server response into a vector of RPSL objects.
/// # Errors
/// Returns nom `Error` if any error occurs during parsing.
pub fn parse_rpsl_server_response(response: &str) -> Result<rpsl::ObjectCollection, Error<&str>> {
    let rpsl_object = many1(component::attribute);
    let empty_or_server_message = alt((component::server_message, tag("\n")));

    let (_, objects) = all_consuming(terminated(
        many1(preceded(many0(empty_or_server_message), rpsl_object)),
        tag("\n"),
    ))(response)
    .finish()?;

    Ok(rpsl::ObjectCollection::from(objects))
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::rpsl;

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
        let expected = rpsl::Object::new(vec![
            rpsl::Attribute::new(
                "role".to_string(),
                vec![Some("Twelve99 Routing Registry".to_string())],
            ),
            rpsl::Attribute::new("remarks".to_string(), vec![None]),
            rpsl::Attribute::new(
                "remarks".to_string(),
                vec![Some("This is a remark.".to_string())],
            ),
            rpsl::Attribute::new(
                "address".to_string(),
                vec![Some("Arelion Sweden AB".to_string())],
            ),
            rpsl::Attribute::new(
                "address".to_string(),
                vec![Some("Evenemangsgatan 2C".to_string())],
            ),
            rpsl::Attribute::new(
                "address".to_string(),
                vec![Some("SE-169 79 SOLNA".to_string())],
            ),
            rpsl::Attribute::new("address".to_string(), vec![Some("Sweden".to_string())]),
            rpsl::Attribute::new(
                "e-mail".to_string(),
                vec![Some("routing-registry@99.net".to_string())],
            ),
            rpsl::Attribute::new("nic-hdl".to_string(), vec![Some("TRR2-RIPE".to_string())]),
            rpsl::Attribute::new(
                "notify".to_string(),
                vec![Some("routing-registry@99.net".to_string())],
            ),
            rpsl::Attribute::new(
                "mnt-by".to_string(),
                vec![Some("Twelve99-IRR-MNT".to_string())],
            ),
            rpsl::Attribute::new(
                "created".to_string(),
                vec![Some("2002-05-27T15:05:16Z".to_string())],
            ),
            rpsl::Attribute::new(
                "last-modified".to_string(),
                vec![Some("2023-01-30T11:49:56Z".to_string())],
            ),
            rpsl::Attribute::new("source".to_string(), vec![Some("RIPE".to_string())]),
        ]);

        assert_eq!(parse_rpsl_object(rpsl).unwrap(), expected);
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
        let expected = rpsl::ObjectCollection::new(vec![
            rpsl::Object::new(vec![
                rpsl::Attribute::new(
                    "as-block".to_string(),
                    vec![Some("AS12557 - AS13223".to_string())],
                ),
                rpsl::Attribute::new(
                    "descr".to_string(),
                    vec![Some("RIPE NCC ASN block".to_string())],
                ),
                rpsl::Attribute::new(
                    "remarks".to_string(),
                    vec![Some(
                        "These AS Numbers are assigned to network operators in the RIPE NCC service region.".to_string(),
                    )],
                ),
                rpsl::Attribute::new(
                    "mnt-by".to_string(),
                    vec![Some("RIPE-NCC-HM-MNT".to_string())],
                ),
                rpsl::Attribute::new(
                    "created".to_string(),
                    vec![Some("2018-11-22T15:27:24Z".to_string())],
                ),
                rpsl::Attribute::new(
                    "last-modified".to_string(),
                    vec![Some("2018-11-22T15:27:24Z".to_string())],
                ),
                rpsl::Attribute::new("source".to_string(), vec![Some("RIPE".to_string())]),
            ]),
            rpsl::Object::new(vec![
                rpsl::Attribute::new("aut-num".to_string(), vec![Some("AS13030".to_string())]),
                rpsl::Attribute::new("as-name".to_string(), vec![Some("INIT7".to_string())]),
                rpsl::Attribute::new("org".to_string(), vec![Some("ORG-ISA1-RIPE".to_string())]),
                rpsl::Attribute::new(
                    "remarks".to_string(),
                    vec![Some("Init7 Global Backbone".to_string())],
                ),
            ]),
            rpsl::Object::new(vec![
                rpsl::Attribute::new(
                    "organisation".to_string(),
                    vec![Some("ORG-ISA1-RIPE".to_string())],
                ),
                rpsl::Attribute::new(
                    "org-name".to_string(),
                    vec![Some("Init7 (Switzerland) Ltd.".to_string())],
                ),
            ]),
        ]);

        assert_eq!(parse_rpsl_server_response(rpsl).unwrap(), expected);
    }
}
