use super::attribute::AttributeView;
use std::ops::Index;

/// A view into an RPSL object in textual representation somewhere in memory.
///
/// This is the borrowed equivalent of an [`Object`], only cointaining references to the
/// original data in the form of [`AttributeView`]s. It presents largely the same interface as
/// its owned equivalent, although it will always return references.
///
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
/// Since an [`ObjectView`] is purely used to provide a view into referenced RPSL data, it can only
/// be created from RPSL text using the [`parse_object`] and [`parse_whois_response`](crate::parse_whois_response) functions.
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
/// assert_eq!(role_acme[0], Attribute::new("role".parse()?, "ACME Company".parse()?));
/// assert_eq!(role_acme[3], Attribute::new("nic-hdl".parse()?, "RPSL1-RIPE".parse()?));
/// # Ok(())
/// # }
/// ```
///
/// While specific attribute values can be accessed by name.
/// ```
/// # use rpsl_parser::{parse_object, Attribute};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = parse_object("
/// # role:           ACME Company
/// # address:        Packet Street 6
/// #                 128 Series of Tubes
/// #                 Internet
/// # email:          rpsl-parser@github.com
/// # nic-hdl:        RPSL1-RIPE
/// # source:         RIPE
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
/// [`Object`]: crate::Object
/// [`parse_object`]: crate::parse_object
/// [`parse_whois_response`]: crate::parse_whois_response
#[derive(Debug, PartialEq, Eq, Clone)]
#[allow(clippy::len_without_is_empty)]
pub struct ObjectView<'a>(Vec<AttributeView<'a>>);

impl<'a> ObjectView<'a> {
    pub(crate) fn new(attributes: Vec<AttributeView<'a>>) -> Self {
        Self(attributes)
    }
    /// The number of attributes referenced within the view.
    #[must_use]
    pub fn len(&self) -> usize {
        self.0.len()
    }
    /// Get the value(s) of specific attribute(s).
    pub fn get(&self, name: &str) -> Vec<&str> {
        let values_matching_name = self.0.iter().filter(|a| a.name == name).map(|a| &a.value);

        let mut values: Vec<&str> = Vec::new();
        for value in values_matching_name {
            match value {
                super::attribute::ValueView::SingleLine(v) => {
                    if let Some(v) = v {
                        values.push(v);
                    }
                }
                super::attribute::ValueView::MultiLine(v) => {
                    values.extend(v.iter().filter_map(Option::as_ref));
                }
            }
        }
        values
    }
}

impl PartialEq<crate::rpsl::Object> for ObjectView<'_> {
    fn eq(&self, other: &crate::rpsl::Object) -> bool {
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
        &self.0[index]
    }
}

impl<'a> IntoIterator for ObjectView<'a> {
    type Item = AttributeView<'a>;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        self.0.into_iter()
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn eq_owned_object_is_eq() {
        let borrowed = ObjectView::new(vec![
            AttributeView::new_single("role", "ACME Company"),
            AttributeView::new_single("address", "Packet Street 6"),
            AttributeView::new_single("address", "128 Series of Tubes"),
            AttributeView::new_single("address", "Internet"),
        ]);
        let owned = crate::rpsl::Object::new(vec![
            crate::rpsl::Attribute::new("role".parse().unwrap(), "ACME Company".parse().unwrap()),
            crate::rpsl::Attribute::new(
                "address".parse().unwrap(),
                "Packet Street 6".parse().unwrap(),
            ),
            crate::rpsl::Attribute::new(
                "address".parse().unwrap(),
                "128 Series of Tubes".parse().unwrap(),
            ),
            crate::rpsl::Attribute::new("address".parse().unwrap(), "Internet".parse().unwrap()),
        ]);
        assert_eq!(borrowed, owned);
    }

    #[test]
    fn ne_owned_object_is_ne() {
        let borrowed = ObjectView::new(vec![
            AttributeView::new_single("role", "Umbrella Corporation"),
            AttributeView::new_single("address", "Paraguas Street"),
            AttributeView::new_single("address", "Racoon City"),
            AttributeView::new_single("address", "Colorado"),
        ]);
        let owned = crate::rpsl::Object::new(vec![
            crate::rpsl::Attribute::new("role".parse().unwrap(), "ACME Company".parse().unwrap()),
            crate::rpsl::Attribute::new(
                "address".parse().unwrap(),
                "Packet Street 6".parse().unwrap(),
            ),
            crate::rpsl::Attribute::new(
                "address".parse().unwrap(),
                "128 Series of Tubes".parse().unwrap(),
            ),
            crate::rpsl::Attribute::new("address".parse().unwrap(), "Internet".parse().unwrap()),
        ]);
        assert_ne!(borrowed, owned);
    }
}
