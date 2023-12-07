use super::attribute::AttributeView;

/// A view into an RPSL object in textual representation somewhere in memory.
///
/// This is the borrowed equivalent of an [`Object`], only cointaining references to the
/// original data in the form of [`AttributeView`]s.
///
/// ```text
/// role:           ACME Company ◀─────────────── &"role"    ───  &"ACME Company"
/// address:        Packet Street 6 ◀──────────── &"address" ─┬─  &"Packet Street 6"
///                 128 Series of Tubes ◀────────             ├─  &"128 Series of Tubes"
///                 Internet ◀───────────────────             └─  &"Internet"
/// email:          rpsl-parser@github.com ◀───── &"email"   ───  &"rpsl-parser@github.com"
/// nic-hdl:        RPSL1-RIPE ◀───────────────── &"nic-hdl" ───  &"RPSL1-RIPE"
/// source:         RIPE ◀─────────────────────── &"source"  ───  &"RIPE"
/// ```
///
/// # Examples
///  
/// Like an owned [`Object`], its attributes can be accessed by index.
/// ```
/// # use rpsl_parser::{parse_object, Attribute};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = parse_object("
/// # role:           ACME Company
/// # address:        Packet Street
/// #                 128 Series of Tubes
/// #                 Internet
/// # email:          rpsl-parser@github.com
/// # nic-hdl:        RPSL1-RIPE
/// # source:         RIPE
/// #
/// # ")?;
/// assert_eq!(role_acme[0], Attribute::new("role", "ACME Company")?);
/// assert_eq!(role_acme[3], Attribute::new("nic-hdl", "RPSL1-RIPE")?);
/// # Ok(())
/// # }
/// ```
///
/// While specific attribute values can be accessed by name.
/// ```
/// # use rpsl_parser::{parse_object, Attribute};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = parse_object("
/// #  role:           ACME Company
/// #  address:        Packet Street
/// #                  128 Series of Tubes
/// #                  Internet
/// #  email:          rpsl-parser@github.com
/// #  nic-hdl:        RPSL1-RIPE
/// #  source:         RIPE
/// #
/// # ")?;
/// assert_eq!(role_acme.get("role"), vec!["ACME Company"]);
/// assert_eq!(role_acme.get("address"), vec!["Packet Street 6", "128 Series of Tubes", "Internet"]);
/// assert_eq!(role_acme.get("email"), vec!["rpsl-parser@github.com"]);
/// assert_eq!(role_acme.get("nic-hdl"), vec!["RPSL1-RIPE"]);
/// assert_eq!(role_acme.get("source"), vec!["RIPE"]);
/// # Ok(())
/// # }
/// ```
#[derive(Debug, PartialEq, Eq, Clone)]
pub struct ObjectView<'a>(Vec<AttributeView<'a>>);

impl<'a> ObjectView<'a> {
    pub(crate) fn new(attributes: Vec<AttributeView<'a>>) -> Self {
        Self(attributes)
    }
}
