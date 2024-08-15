use super::attribute::AttributeView;
use std::{
    fmt,
    ops::{Deref, Index},
};

/// A view into an RPSL object in textual representation somewhere in memory.
///
/// This is the borrowed equivalent of an [`Object`], only containing references to the
/// original data in the form of [`AttributeView`]s. It presents largely the same interface as
/// its owned equivalent, although it will always return references.
///
///
/// ```text
/// role:           ACME Company ◀─────────────── &"role"    ───  &"ACME Company"
/// address:        Packet Street 6 ◀──────────── &"address" ─┬─  &"Packet Street 6"
///                 128 Series of Tubes ◀────────             ├─  &"128 Series of Tubes"
///                 Internet ◀───────────────────             └─  &"Internet"
/// email:          rpsl-rs@github.com ◀───────── &"email"   ───  &"rpsl-rs@github.com"
/// nic-hdl:        RPSL1-RIPE ◀───────────────── &"nic-hdl" ───  &"RPSL1-RIPE"
/// source:         RIPE ◀─────────────────────── &"source"  ───  &"RIPE"
/// ```
///
/// Since an [`ObjectView`] is purely used to provide a view into referenced RPSL data, it can only
/// be created from RPSL text using the [`parse_object`] and [`parse_whois_response`](crate::parse_whois_response) functions.
///
/// # Examples
///  
/// Like an owned [`Object`], its attributes can be accessed by index.
/// ```
/// # use rpsl::{parse_object, Attribute};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = parse_object("
/// # role:           ACME Company
/// # address:        Packet Street
/// #                 128 Series of Tubes
/// #                 Internet
/// # email:          rpsl-rs@github.com
/// # nic-hdl:        RPSL1-RIPE
/// # source:         RIPE
/// #
/// # ")?;
/// assert_eq!(role_acme[0], Attribute::new("role".parse()?, "ACME Company".parse()?));
/// assert_eq!(role_acme[3], Attribute::new("nic-hdl".parse()?, "RPSL1-RIPE".parse()?));
/// # Ok(())
/// # }
/// ```
///
/// While specific attribute values can be accessed by name.
/// ```
/// # use rpsl::{parse_object, Attribute};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = parse_object("
/// # role:           ACME Company
/// # address:        Packet Street 6
/// #                 128 Series of Tubes
/// #                 Internet
/// # email:          rpsl-rs@github.com
/// # nic-hdl:        RPSL1-RIPE
/// # source:         RIPE
/// #
/// # ")?;
/// assert_eq!(role_acme.get("role"), vec!["ACME Company"]);
/// assert_eq!(role_acme.get("address"), vec!["Packet Street 6", "128 Series of Tubes", "Internet"]);
/// assert_eq!(role_acme.get("email"), vec!["rpsl-rs@github.com"]);
/// assert_eq!(role_acme.get("nic-hdl"), vec!["RPSL1-RIPE"]);
/// assert_eq!(role_acme.get("source"), vec!["RIPE"]);
/// # Ok(())
/// # }
/// ```
///
/// Views can be compared to their owned equivalents.
/// ```
/// # use rpsl::{parse_object, Attribute, object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = parse_object("
/// # role:           ACME Company
/// # address:        Packet Street 6
/// #                 128 Series of Tubes
/// #                 Internet
/// # email:          rpsl-rs@github.com
/// # nic-hdl:        RPSL1-RIPE
/// # source:         RIPE
/// #
/// # ")?;
/// assert_eq!(
///     role_acme,
///     object! {
///         "role": "ACME Company";
///         "address": "Packet Street 6", "128 Series of Tubes", "Internet";
///         "email": "rpsl-rs@github.com";
///         "nic-hdl": "RPSL1-RIPE";
///         "source": "RIPE";
///      },
/// );
/// # Ok(())
/// # }
/// ```
///
/// As well as converted to them if required.
/// ```
/// # use rpsl::{parse_object, Attribute};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = parse_object("
/// # role:           ACME Company
/// # address:        Packet Street 6
/// #                 128 Series of Tubes
/// #                 Internet
/// # email:          rpsl-rs@github.com
/// # nic-hdl:        RPSL1-RIPE
/// # source:         RIPE
/// #
/// # ")?;
/// role_acme.to_owned();
/// # Ok(())
/// # }
/// ```
/// [`Object`]: crate::Object
/// [`parse_object`]: crate::parse_object
/// [`parse_whois_response`]: crate::parse_whois_response
#[derive(Clone)]
#[allow(clippy::len_without_is_empty)]
pub struct ObjectView<'a> {
    attributes: Vec<AttributeView<'a>>,
    /// The original RPSL text that was parsed to create this view.
    source: &'a str,
}

impl<'a> ObjectView<'a> {
    pub(crate) fn new(attributes: Vec<AttributeView<'a>>, source: &'a str) -> Self {
        Self { attributes, source }
    }

    /// Turn the view into an owned [`Object`](crate::Object).
    pub fn to_owned(&self) -> crate::Object {
        crate::Object::new(
            self.attributes
                .iter()
                .map(AttributeView::to_owned)
                .collect(),
        )
    }

    /// The number of attributes referenced within the view.
    #[must_use]
    pub fn len(&self) -> usize {
        self.attributes.len()
    }

    /// Get the value(s) of specific attribute(s).
    pub fn get(&self, name: &str) -> Vec<&str> {
        self.attributes
            .iter()
            .filter(|a| a.name == name)
            .flat_map(|a| a.value.with_content())
            .collect()
    }
}

impl PartialEq for ObjectView<'_> {
    fn eq(&self, other: &Self) -> bool {
        self.attributes == other.attributes
    }
}

impl PartialEq<crate::Object> for ObjectView<'_> {
    fn eq(&self, other: &crate::Object) -> bool {
        // TODO: Avoid cloning
        for (s, o) in self.clone().into_iter().zip(other.clone().into_iter()) {
            if s != o {
                return false;
            }
        }
        true
    }
}

impl<'a> Index<usize> for ObjectView<'a> {
    type Output = AttributeView<'a>;

    fn index(&self, index: usize) -> &Self::Output {
        &self.attributes[index]
    }
}

impl<'a> Deref for ObjectView<'a> {
    type Target = Vec<AttributeView<'a>>;

    fn deref(&self) -> &Self::Target {
        &self.attributes
    }
}

impl<'a> IntoIterator for ObjectView<'a> {
    type Item = AttributeView<'a>;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        self.attributes.into_iter()
    }
}

impl fmt::Debug for ObjectView<'_> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:#?}", self.attributes)
    }
}

impl fmt::Display for ObjectView<'_> {
    /// Display the view as it's original RPSL.
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.source)
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    /// Views with equal attributes evaluate as equal, regardless of trailing newline.
    fn eq_views_are_eq() {
        let view_1 = ObjectView::new(
            vec![
                AttributeView::new_single("role", "ACME Company"),
                AttributeView::new_single("address", "Packet Street 6"),
                AttributeView::new_single("address", "128 Series of Tubes"),
                AttributeView::new_single("address", "Internet"),
            ],
            concat!(
                "role:           ACME Company\n",
                "address:        Packet Street 6\n",
                "address:        128 Series of Tubes\n",
                "address:        Internet\n",
                "\n" // Correctly terminated by a trailing newline.
            ),
        );
        let view_1_no_trailing_newline = ObjectView::new(
            vec![
                AttributeView::new_single("role", "ACME Company"),
                AttributeView::new_single("address", "Packet Street 6"),
                AttributeView::new_single("address", "128 Series of Tubes"),
                AttributeView::new_single("address", "Internet"),
            ],
            concat!(
                "role:           ACME Company\n",
                "address:        Packet Street 6\n",
                "address:        128 Series of Tubes\n",
                "address:        Internet\n",
                // Missing a trailing newline.
            ),
        );

        assert_eq!(view_1, view_1);
        assert_eq!(view_1, view_1_no_trailing_newline);
    }

    #[test]
    /// Views that have different attributes do not evaluate as equal.
    fn ne_views_are_ne() {
        let view_1 = ObjectView::new(
            vec![
                AttributeView::new_single("role", "Umbrella Corporation"),
                AttributeView::new_single("address", "Paraguas Street"),
                AttributeView::new_single("address", "Raccoon City"),
                AttributeView::new_single("address", "Colorado"),
            ],
            concat!(
                "role:           Umbrella Corporation\n",
                "address:        Paraguas Street\n",
                "address:        Raccoon City\n",
                "address:        Colorado\n",
                "\n"
            ),
        );
        let view_2 = ObjectView::new(
            vec![
                AttributeView::new_single("role", "ACME Company"),
                AttributeView::new_single("address", "Packet Street 6"),
                AttributeView::new_single("address", "128 Series of Tubes"),
                AttributeView::new_single("address", "Internet"),
            ],
            concat!(
                "role:           ACME Company\n",
                "address:        Packet Street 6\n",
                "address:        128 Series of Tubes\n",
                "address:        Internet\n",
                "\n"
            ),
        );

        assert_ne!(view_1, view_2);
    }

    #[test]
    /// Views and owned objects with the same attributes evaluate as equal.
    fn eq_view_and_owned_object_is_eq() {
        let object_1_borrowed = ObjectView::new(
            vec![
                AttributeView::new_single("role", "ACME Company"),
                AttributeView::new_single("address", "Packet Street 6"),
                AttributeView::new_single("address", "128 Series of Tubes"),
                AttributeView::new_single("address", "Internet"),
            ],
            "FAKE TEST VALUE",
        );
        let object_1_owned = crate::Object::new(vec![
            crate::Attribute::new("role".parse().unwrap(), "ACME Company".parse().unwrap()),
            crate::Attribute::new(
                "address".parse().unwrap(),
                "Packet Street 6".parse().unwrap(),
            ),
            crate::Attribute::new(
                "address".parse().unwrap(),
                "128 Series of Tubes".parse().unwrap(),
            ),
            crate::Attribute::new("address".parse().unwrap(), "Internet".parse().unwrap()),
        ]);
        assert_eq!(object_1_borrowed, object_1_owned);
    }

    #[test]
    /// Views and owned objects that have different attributes do not evaluate as equal.
    fn ne_view_and_owned_object_is_ne() {
        let object_1_borrowed = ObjectView::new(
            vec![
                AttributeView::new_single("role", "Umbrella Corporation"),
                AttributeView::new_single("address", "Paraguas Street"),
                AttributeView::new_single("address", "Raccoon City"),
                AttributeView::new_single("address", "Colorado"),
            ],
            "FAKE TEST VALUE",
        );
        let object_2_owned = crate::Object::new(vec![
            crate::Attribute::new("role".parse().unwrap(), "ACME Company".parse().unwrap()),
            crate::Attribute::new(
                "address".parse().unwrap(),
                "Packet Street 6".parse().unwrap(),
            ),
            crate::Attribute::new(
                "address".parse().unwrap(),
                "128 Series of Tubes".parse().unwrap(),
            ),
            crate::Attribute::new("address".parse().unwrap(), "Internet".parse().unwrap()),
        ]);
        assert_ne!(object_1_borrowed, object_2_owned);
    }
}
