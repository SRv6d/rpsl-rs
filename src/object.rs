use std::{
    borrow::Cow,
    fmt,
    ops::{Deref, Index},
};

#[cfg(feature = "serde")]
use serde::Serialize;

use super::Attribute;
use crate::spec::{AttributeError, Raw, Specification};

/// A RPSL object.
///
/// ```text
/// ┌───────────────────────────────────────────────┐
/// │  Object                                       │
/// ├───────────────────────────────────────────────┤
/// │  [role]    ──── ACME Company                  │
/// │  [address] ──┬─ Packet Street 6               │
/// │              ├─ 128 Series of Tubes           │
/// │              └─ Internet                      │
/// │  [email]   ──── rpsl-rs@github.com            │
/// │  [nic-hdl] ──── RPSL1-RIPE                    │
/// │  [source]  ──── RIPE                          │
/// └───────────────────────────────────────────────┘
/// ```
///
/// # Examples
///
/// A role object for the ACME corporation.
/// ```
/// # use rpsl::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let role_acme = Object::new(vec![
///     Attribute::new("role", "ACME Company"),
///     Attribute::new("address", "Packet Street 6"),
///     Attribute::new("address", "128 Series of Tubes"),
///     Attribute::new("address", "Internet"),
///     Attribute::new("email", "rpsl-rs@github.com"),
///     Attribute::new("nic-hdl", "RPSL1-RIPE"),
///     Attribute::new("source", "RIPE"),
/// ]);
/// # Ok(())
/// # }
/// ```
///
/// Although creating an [`Object`] from a vector of [`Attribute`]s works, the easier way
/// to do it is by using the [`object!`](crate::object!) macro.
/// ```
/// # use rpsl::{Attribute, Object, object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role", "ACME Company"),
/// #     Attribute::new("address", "Packet Street 6"),
/// #     Attribute::new("address", "128 Series of Tubes"),
/// #     Attribute::new("address", "Internet"),
/// #     Attribute::new("email", "rpsl-rs@github.com"),
/// #     Attribute::new("nic-hdl", "RPSL1-RIPE"),
/// #     Attribute::new("source", "RIPE"),
/// # ]);
/// assert_eq!(
///     role_acme,
///     object! {
///         "role": "ACME Company";
///         "address": "Packet Street 6";
///         "address": "128 Series of Tubes";
///         "address": "Internet";
///         "email": "rpsl-rs@github.com";
///         "nic-hdl": "RPSL1-RIPE";
///         "source": "RIPE";
///     },
/// );
/// # Ok(())
/// # }
/// ```
///
/// Each attribute can be accessed by index.
/// ```
/// # use rpsl::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role", "ACME Company"),
/// #     Attribute::new("address", "Packet Street 6"),
/// #     Attribute::new("address", "128 Series of Tubes"),
/// #     Attribute::new("address", "Internet"),
/// #     Attribute::new("email", "rpsl-rs@github.com"),
/// #     Attribute::new("nic-hdl", "RPSL1-RIPE"),
/// #     Attribute::new("source", "RIPE"),
/// # ]);
/// assert_eq!(role_acme[0], Attribute::new("role", "ACME Company"));
/// assert_eq!(role_acme[6], Attribute::new("source", "RIPE"));
/// # Ok(())
/// # }
/// ```
///
/// While specific attribute values can be accessed by name.
/// ```
/// # use rpsl::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role", "ACME Company"),
/// #     Attribute::new("address", "Packet Street 6"),
/// #     Attribute::new("address", "128 Series of Tubes"),
/// #     Attribute::new("address", "Internet"),
/// #     Attribute::new("email", "rpsl-rs@github.com"),
/// #     Attribute::new("nic-hdl", "RPSL1-RIPE"),
/// #     Attribute::new("source", "RIPE"),
/// # ]);
/// assert_eq!(role_acme.get("role"), vec!["ACME Company"]);
/// assert_eq!(role_acme.get("address"), vec!["Packet Street 6", "128 Series of Tubes", "Internet"]);
/// assert_eq!(role_acme.get("email"), vec!["rpsl-rs@github.com"]);
/// assert_eq!(role_acme.get("nic-hdl"), vec!["RPSL1-RIPE"]);
/// assert_eq!(role_acme.get("source"), vec!["RIPE"]);
/// # Ok(())
/// # }
/// ```
///
/// The entire object can also be represented as RPSL.
/// ```
/// # use rpsl::{Attribute, Object};
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role", "ACME Company"),
/// #     Attribute::new("address", "Packet Street 6"),
/// #     Attribute::new("address", "128 Series of Tubes"),
/// #     Attribute::new("address", "Internet"),
/// #     Attribute::new("email", "rpsl-rs@github.com"),
/// #     Attribute::new("nic-hdl", "RPSL1-RIPE"),
/// #     Attribute::new("source", "RIPE"),
/// # ]);
/// assert_eq!(
///    role_acme.to_string(),
///    concat!(
///        "role:           ACME Company\n",
///        "address:        Packet Street 6\n",
///        "address:        128 Series of Tubes\n",
///        "address:        Internet\n",
///        "email:          rpsl-rs@github.com\n",
///        "nic-hdl:        RPSL1-RIPE\n",
///        "source:         RIPE\n",
///        "\n"
///    )
/// );
/// # Ok(())
/// # }
/// ```
///
/// Or serialized to JSON if the corresponding feature is enabled.
/// ```
/// # use rpsl::{Attribute, Object};
/// # #[cfg(feature = "json")]
/// # use serde_json::json;
/// # let role_acme = Object::new(vec![
/// #     Attribute::new("role", "ACME Company"),
/// #     Attribute::new("address", "Packet Street 6"),
/// #     Attribute::new("address", "128 Series of Tubes"),
/// #     Attribute::new("address", "Internet"),
/// #     Attribute::new("email", "rpsl-rs@github.com"),
/// #     Attribute::new("nic-hdl", "RPSL1-RIPE"),
/// #     Attribute::new("source", "RIPE"),
/// # ]);
/// # #[cfg(feature = "json")]
/// assert_eq!(
///    role_acme.json(),
///    json!({
///        "attributes": [
///            { "name": "role", "values": ["ACME Company"] },
///            { "name": "address", "values": ["Packet Street 6"] },
///            { "name": "address", "values": ["128 Series of Tubes"] },
///            { "name": "address", "values": ["Internet"] },
///            { "name": "email", "values": ["rpsl-rs@github.com"] },
///            { "name": "nic-hdl", "values": ["RPSL1-RIPE"] },
///            { "name": "source", "values": ["RIPE"] }
///        ]
///    })
/// );
/// # Ok::<(), Box<dyn std::error::Error>>(())
/// ```
#[derive(Debug, Clone)]
#[cfg_attr(feature = "serde", derive(Serialize), serde(bound = ""))]
#[allow(clippy::len_without_is_empty)]
pub struct Object<'a, Spec: Specification = Raw> {
    attributes: Vec<Attribute<'a, Spec>>,
    /// Contains the source if the object was created by parsing RPSL.
    #[cfg_attr(feature = "serde", serde(skip))]
    source: Option<Cow<'a, str>>,
}

impl<'a, Spec: Specification> Object<'a, Spec> {
    /// Validate that all attributes of this object conform to a target specification.
    ///
    /// # Errors
    /// Returns an [`ObjectValidationError`] if any attribute fails to satisfy the target specification.
    ///
    /// # Examples
    /// ```
    /// # use rpsl::{object, spec::Rfc2622};
    /// let obj = object! {
    ///     "role": "ACME Company";
    ///     "address": "Packet Street 6";
    /// };
    /// obj.validate::<Rfc2622>()?;
    /// # Ok::<(), Box<dyn std::error::Error>>(())
    /// ```
    pub fn validate<TargetSpec: Specification>(&self) -> Result<(), ObjectValidationError> {
        let mut errors = Vec::new();
        for (index, attribute) in self.attributes.iter().enumerate() {
            if let Err(error) = attribute.validate::<TargetSpec>() {
                errors.push((index, error));
            }
        }

        if errors.is_empty() {
            Ok(())
        } else {
            Err(ObjectValidationError::new(errors))
        }
    }

    /// Convert every attribute in this object into a target specification.
    ///
    /// # Errors
    /// Returns the first [`AttributeError`] encountered. Use [`Object::validate`] to collect
    /// all attribute errors before converting.
    ///
    /// # Examples
    /// ```
    /// # use rpsl::{object, Object, spec::Rfc2622};
    /// let obj = object! {
    ///     "role": "ACME Company";
    /// };
    /// let validated: Object<Rfc2622> = obj.into_spec()?;
    /// # Ok::<(), Box<dyn std::error::Error>>(())
    /// ```
    pub fn into_spec<TargetSpec: Specification>(
        self,
    ) -> Result<Object<'a, TargetSpec>, AttributeError> {
        let Object { attributes, source } = self;

        let mut converted = Vec::with_capacity(attributes.len());
        for attribute in attributes {
            converted.push(attribute.into_spec::<TargetSpec>()?);
        }

        Ok(Object {
            attributes: converted,
            source,
        })
    }

    /// Create a new RPSL object from a vector of attributes.
    ///
    /// # Example
    /// ```
    /// # use rpsl::{Attribute, Object};
    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
    /// let role_acme = Object::new(vec![
    ///     Attribute::new("role", "ACME Company"),
    ///     Attribute::new("address", "Packet Street 6"),
    ///     Attribute::new("address", "128 Series of Tubes"),
    ///     Attribute::new("address", "Internet"),
    ///     Attribute::new("email", "rpsl-rs@github.com"),
    ///     Attribute::new("nic-hdl", "RPSL1-RIPE"),
    ///     Attribute::new("source", "RIPE"),
    /// ]);
    /// # Ok(())
    /// # }
    /// ```
    #[must_use]
    pub fn new(attributes: Vec<Attribute<'static, Spec>>) -> Object<'static, Spec> {
        Object {
            attributes,
            source: None,
        }
    }

    /// Create a new RPSL object from a text source and it's corresponding parsed attributes.
    pub(crate) fn new_parsed(
        source: &'a str,
        attributes: Vec<Attribute<'a, Spec>>,
    ) -> Object<'a, Spec> {
        Object {
            attributes,
            source: Some(Cow::Borrowed(source)),
        }
    }

    /// The number of attributes in the object.
    #[must_use]
    pub fn len(&self) -> usize {
        self.attributes.len()
    }

    /// Get the value(s) of specific attribute(s).
    #[must_use]
    pub fn get(&self, name: &str) -> Vec<&str> {
        self.attributes
            .iter()
            .filter(|a| a.name == name)
            .flat_map(|a| a.value.with_content())
            .collect()
    }

    #[cfg(feature = "json")]
    #[cfg_attr(docsrs, doc(cfg(feature = "json")))]
    #[allow(clippy::missing_panics_doc)]
    #[must_use]
    /// Serialize the object into a JSON value.
    pub fn json(&self) -> serde_json::Value {
        serde_json::to_value(self).unwrap()
    }

    /// Access the source field for use in tests.
    #[cfg(test)]
    pub(crate) fn source(&self) -> Option<&str> {
        self.source.as_deref()
    }

    /// Convert this object into an owned (`'static`) variant.
    pub fn into_owned(self) -> Object<'static, Spec> {
        Object {
            attributes: self
                .attributes
                .into_iter()
                .map(Attribute::into_owned)
                .collect(),
            source: self.source.map(|s| Cow::Owned(s.into_owned())),
        }
    }
}

impl<'a, Spec: Specification> Index<usize> for Object<'a, Spec> {
    type Output = Attribute<'a, Spec>;

    fn index(&self, index: usize) -> &Self::Output {
        &self.attributes[index]
    }
}

impl<'a, Spec: Specification> Deref for Object<'a, Spec> {
    type Target = Vec<Attribute<'a, Spec>>;

    fn deref(&self) -> &Self::Target {
        &self.attributes
    }
}

impl<'a, Spec: Specification> IntoIterator for Object<'a, Spec> {
    type Item = Attribute<'a, Spec>;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        self.attributes.into_iter()
    }
}

impl PartialEq for Object<'_> {
    /// Compare two objects.
    /// Since objects that are semantically equal may display differently, only `PartialEq` is implemented.
    fn eq(&self, other: &Self) -> bool {
        self.attributes == other.attributes
    }
}

impl fmt::Display for Object<'_> {
    /// Display the object as RPSL.
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        if let Some(source) = &self.source {
            write!(f, "{source}")
        } else {
            for attribute in &self.attributes {
                write!(f, "{attribute}")?;
            }
            writeln!(f)
        }
    }
}

/// Creates an [`Object`] containing the given attributes.
///
/// - Create an [`Object`] containing only single value attributes:
/// ```
/// # use rpsl::object;
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let obj = object! {
///     "role": "ACME Company";
///     "address": "Packet Street 6";
///     "address": "128 Series of Tubes";
///     "address": "Internet";
/// };
/// assert_eq!(obj[0].name, "role");
/// assert_eq!(obj[0].value, "ACME Company");
/// assert_eq!(obj[1].name, "address");
/// assert_eq!(obj[1].value, "Packet Street 6");
/// assert_eq!(obj[2].name, "address");
/// assert_eq!(obj[2].value, "128 Series of Tubes");
/// assert_eq!(obj[3].name, "address");
/// assert_eq!(obj[3].value, "Internet");
/// # Ok(())
/// # }
/// ```
///
/// - Create an `Object` containing multi value attributes:
/// ```
/// # use rpsl::object;
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let obj = object! {
///    "role": "ACME Company";
///    "address": "Packet Street 6", "128 Series of Tubes", "Internet";
/// };
/// assert_eq!(obj[0].name, "role");
/// assert_eq!(obj[0].value, "ACME Company");
/// assert_eq!(obj[1].name, "address");
/// assert_eq!(obj[1].value, vec!["Packet Street 6", "128 Series of Tubes", "Internet"]);
/// # Ok(())
/// # }
#[macro_export]
macro_rules! object {
    (
        $(
            $name:literal: $($value:literal),+
        );+ $(;)?
    ) => {
        $crate::Object::new(vec![
            $(
                {
                    let name = $crate::Name::new($name);
                    let value: $crate::Value = vec![$($value),+].into();
                    $crate::Attribute::new(name, value)
                },
            )*
        ])
    };
}

/// Contains all attribute validation errors for an [`Object`].
#[derive(Debug, thiserror::Error)]
#[error("{num} attribute(s) failed validation", num = .errors.len())]
pub struct ObjectValidationError {
    /// Validation errors paired with the index of the offending attribute.
    errors: Vec<(usize, AttributeError)>,
}

impl ObjectValidationError {
    fn new(errors: Vec<(usize, AttributeError)>) -> Self {
        Self { errors }
    }

    /// The number of attributes that failed validation.
    #[must_use]
    pub fn len(&self) -> usize {
        self.errors.len()
    }

    /// Returns `true` if no attribute validation errors are contained.
    #[must_use]
    pub fn is_empty(&self) -> bool {
        self.errors.is_empty()
    }

    /// Iterate over the attribute errors.
    pub fn iter_errors(&self) -> impl Iterator<Item = &AttributeError> {
        self.errors.iter().map(|(_, error)| error)
    }

    /// Iterate over attribute errors together with the index of the offending attribute.
    pub fn iter_indexed(&self) -> impl Iterator<Item = (usize, &AttributeError)> {
        self.errors.iter().map(|(index, error)| (*index, error))
    }

    /// Return attribute errors together with the index of the offending attribute.
    #[must_use]
    pub fn into_errors(self) -> Vec<(usize, AttributeError)> {
        self.errors
    }
}

#[cfg(test)]
mod tests {
    use rstest::*;
    #[cfg(feature = "json")]
    use serde_json::json;

    use super::*;
    use crate::{
        spec::{InvalidNameError, Rfc2622},
        Name,
    };

    #[rstest]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_single("address", "Packet Street 6"),
            Attribute::unchecked_single("address", "128 Series of Tubes"),
            Attribute::unchecked_single("address", "Internet"),
            Attribute::unchecked_single("email", "rpsl-rs@github.com"),
            Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
            Attribute::unchecked_single("source", "RIPE"),
        ]),
        Object::new_parsed(
            concat!(
                "role:           ACME Company\n",
                "address:        Packet Street 6\n",
                "address:        128 Series of Tubes\n",
                "address:        Internet\n",
                "email:          rpsl-rs@github.com\n",
                "nic-hdl:        RPSL1-RIPE\n",
                "source:         RIPE\n",
                "\n"
            ),
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_single("address", "Packet Street 6"),
                Attribute::unchecked_single("address", "128 Series of Tubes"),
                Attribute::unchecked_single("address", "Internet"),
                Attribute::unchecked_single("email", "rpsl-rs@github.com"),
                Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
                Attribute::unchecked_single("source", "RIPE"),
            ]
        ),
        concat!(
            "role:           ACME Company\n",
            "address:        Packet Street 6\n",
            "address:        128 Series of Tubes\n",
            "address:        Internet\n",
            "email:          rpsl-rs@github.com\n",
            "nic-hdl:        RPSL1-RIPE\n",
            "source:         RIPE\n",
            "\n"
        )
    )]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_multi(
                "address",
                ["Packet Street 6", "128 Series of Tubes", "Internet"]
            ),
            Attribute::unchecked_single("email", "rpsl-rs@github.com"),
            Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
            Attribute::unchecked_single("source", "RIPE"),
        ]),
        Object::new_parsed(
            concat!(
                "role:           ACME Company\n",
                "address:        Packet Street 6\n",
                "                128 Series of Tubes\n",
                "                Internet\n",
                "email:          rpsl-rs@github.com\n",
                "nic-hdl:        RPSL1-RIPE\n",
                "source:         RIPE\n",
                "\n"
            ),
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_multi(
                    "address",
                    ["Packet Street 6", "128 Series of Tubes", "Internet"]
                ),
                Attribute::unchecked_single("email", "rpsl-rs@github.com"),
                Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
                Attribute::unchecked_single("source", "RIPE"),
            ]
        ),
        concat!(
            "role:           ACME Company\n",
            "address:        Packet Street 6\n",
            "                128 Series of Tubes\n",
            "                Internet\n",
            "email:          rpsl-rs@github.com\n",
            "nic-hdl:        RPSL1-RIPE\n",
            "source:         RIPE\n",
            "\n"
        )
    )]
    fn object_display(
        #[case] owned: Object<'static>,
        #[case] borrowed: Object,
        #[case] expected: &str,
    ) {
        assert_eq!(owned.to_string(), expected);
        assert_eq!(borrowed.to_string(), expected);
    }

    #[rstest]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
        ]),
        1
    )]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_single("address", "Packet Street 6"),
            Attribute::unchecked_single("address", "128 Series of Tubes"),
            Attribute::unchecked_single("address", "Internet"),
            Attribute::unchecked_single("email", "rpsl-rs@github.com"),
            Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
            Attribute::unchecked_single("source", "RIPE"),
        ]),
        7
    )]
    fn object_len(#[case] object: Object, #[case] expected: usize) {
        assert_eq!(object.len(), expected);
    }

    #[rstest]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_single("address", "Packet Street 6"),
            Attribute::unchecked_single("address", "128 Series of Tubes"),
            Attribute::unchecked_single("address", "Internet"),
            Attribute::unchecked_single("email", "rpsl-rs@github.com"),
            Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
            Attribute::unchecked_single("source", "RIPE"),
        ]),
        2,
        Attribute::unchecked_single("address", "128 Series of Tubes"),
    )]
    fn object_index(#[case] object: Object, #[case] index: usize, #[case] expected: Attribute) {
        assert_eq!(object[index], expected);
    }

    #[rstest]
    #[case(
        vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_single("address", "Packet Street 6"),
            Attribute::unchecked_single("address", "128 Series of Tubes"),
            Attribute::unchecked_single("address", "Internet"),
            Attribute::unchecked_single("email", "rpsl-rs@github.com"),
            Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
            Attribute::unchecked_single("source", "RIPE"),
        ],
    )]
    fn object_deref(#[case] attributes: Vec<Attribute<'static>>) {
        let object = Object::new(attributes.clone());
        assert_eq!(*object, attributes);
    }

    #[rstest]
    #[case(
        vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_single("address", "Packet Street 6"),
            Attribute::unchecked_single("address", "128 Series of Tubes"),
            Attribute::unchecked_single("address", "Internet"),
            Attribute::unchecked_single("email", "rpsl-rs@github.com"),
            Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
            Attribute::unchecked_single("source", "RIPE"),
        ],
    )]
    fn object_into_iter(#[case] attributes: Vec<Attribute<'static>>) {
        let object = Object::new(attributes.clone());

        let attr_iter = attributes.into_iter();
        let obj_iter = object.into_iter();

        for (a, b) in attr_iter.zip(obj_iter) {
            assert_eq!(a, b);
        }
    }

    #[rstest]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_single("address", "Packet Street 6"),
            Attribute::unchecked_single("address", "128 Series of Tubes"),
            Attribute::unchecked_single("address", "Internet"),
            Attribute::unchecked_single("email", "rpsl-rs@github.com"),
            Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
            Attribute::unchecked_single("source", "RIPE"),
        ]),
        json!({
            "attributes": [
                { "name": "role", "values": ["ACME Company"] },
                { "name": "address", "values": ["Packet Street 6"] },
                { "name": "address", "values": ["128 Series of Tubes"] },
                { "name": "address", "values": ["Internet"] },
                { "name": "email", "values": ["rpsl-rs@github.com"] },
                { "name": "nic-hdl", "values": ["RPSL1-RIPE"] },
                { "name": "source", "values": ["RIPE"] }
            ]
        })
    )]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_multi(
                "address",
                ["Packet Street 6", "", "128 Series of Tubes", "Internet"]
            ),
            Attribute::unchecked_single("email", "rpsl-rs@github.com"),
            Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
            Attribute::unchecked_single("source", "RIPE"),
        ]),
        json!({
            "attributes": [
                { "name": "role", "values": ["ACME Company"] },
                {
                    "name": "address",
                    "values": ["Packet Street 6", null, "128 Series of Tubes", "Internet"] },
                { "name": "email", "values": ["rpsl-rs@github.com"] },
                { "name": "nic-hdl", "values": ["RPSL1-RIPE"] },
                { "name": "source", "values": ["RIPE"] }
            ]
        })
    )]
    #[cfg(feature = "json")]
    fn object_json_repr(#[case] object: Object, #[case] expected: serde_json::Value) {
        let json = object.json();
        assert_eq!(json, expected);
    }

    #[rstest]
    #[case(
        Object::new_parsed(
            concat!(
                "role:           ACME Company\n",
                "address:        Packet Street 6\n",
                "address:        128 Series of Tubes\n",
                "address:        Internet\n",
                "email:          rpsl-rs@github.com\n",
                "nic-hdl:        RPSL1-RIPE\n",
                "source:         RIPE\n",
                "\n", // Terminated by a trailing newline.
            ),
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_single("address", "Packet Street 6"),
                Attribute::unchecked_single("address", "128 Series of Tubes"),
                Attribute::unchecked_single("address", "Internet"),
                Attribute::unchecked_single("email", "rpsl-rs@github.com"),
                Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
                Attribute::unchecked_single("source", "RIPE"),
            ],
        ),
        concat!(
            "role:           ACME Company\n",
            "address:        Packet Street 6\n",
            "address:        128 Series of Tubes\n",
            "address:        Internet\n",
            "email:          rpsl-rs@github.com\n",
            "nic-hdl:        RPSL1-RIPE\n",
            "source:         RIPE\n",
            "\n" // Contains a trailing newline.
        )
    )]
    #[case(
        Object::new_parsed(
            concat!(
                "role:           ACME Company\n",
                "address:        Packet Street 6\n",
                "address:        128 Series of Tubes\n",
                "address:        Internet\n",
                "email:          rpsl-rs@github.com\n",
                "nic-hdl:        RPSL1-RIPE\n",
                "source:         RIPE\n",
                // Not terminated by a trailing newline.
            ),
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_single("address", "Packet Street 6"),
                Attribute::unchecked_single("address", "128 Series of Tubes"),
                Attribute::unchecked_single("address", "Internet"),
                Attribute::unchecked_single("email", "rpsl-rs@github.com"),
                Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
                Attribute::unchecked_single("source", "RIPE"),
            ],
        ),
        concat!(
            "role:           ACME Company\n",
            "address:        Packet Street 6\n",
            "address:        128 Series of Tubes\n",
            "address:        Internet\n",
            "email:          rpsl-rs@github.com\n",
            "nic-hdl:        RPSL1-RIPE\n",
            "source:         RIPE\n",
            // Does not contain a trailing newline.
        )
    )]
    #[case(
        Object::new_parsed(
            concat!(
                "role:           ACME Company\n",
                "address:        Packet Street 6\n",
                // Using space as a continuation char.
                "                128 Series of Tubes\n",
                "                Internet\n",
                "email:          rpsl-rs@github.com\n",
                "nic-hdl:        RPSL1-RIPE\n",
                "source:         RIPE\n",
                "\n"
            ),
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_multi(
                    "address",
                    ["Packet Street 6", "128 Series of Tubes", "Internet"]
                ),
                Attribute::unchecked_single("email", "rpsl-rs@github.com"),
                Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
                Attribute::unchecked_single("source", "RIPE"),
            ],
        ),
        concat!(
            "role:           ACME Company\n",
            "address:        Packet Street 6\n",
            // Using space as a continuation char.
            "                128 Series of Tubes\n",
            "                Internet\n",
            "email:          rpsl-rs@github.com\n",
            "nic-hdl:        RPSL1-RIPE\n",
            "source:         RIPE\n",
            "\n"
        )
    )]
    #[case(
        Object::new_parsed(
            concat!(
                "role:           ACME Company\n",
                "address:        Packet Street 6\n",
                // Using + as a continuation char.
                "+               128 Series of Tubes\n",
                "+               Internet\n",
                "email:          rpsl-rs@github.com\n",
                "nic-hdl:        RPSL1-RIPE\n",
                "source:         RIPE\n",
                "\n"
            ),
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_multi(
                    "address",
                    ["Packet Street 6", "128 Series of Tubes", "Internet"]
                ),
                Attribute::unchecked_single("email", "rpsl-rs@github.com"),
                Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
                Attribute::unchecked_single("source", "RIPE"),
            ],
        ),
        concat!(
            "role:           ACME Company\n",
            "address:        Packet Street 6\n",
            // Using + as a continuation char.
            "+               128 Series of Tubes\n",
            "+               Internet\n",
            "email:          rpsl-rs@github.com\n",
            "nic-hdl:        RPSL1-RIPE\n",
            "source:         RIPE\n",
            "\n"
        )
    )]
    /// Borrowed objects display as the original RPSL they were created from.
    fn borrowed_objects_display_like_source(#[case] object: Object, #[case] expected: &str) {
        assert_eq!(object.to_string(), expected);
    }

    #[rstest]
    #[case(
        object! {
            "role": "ACME Company";
            "address": "Packet Street 6", "128 Series of Tubes", "Internet";
            "email": "rpsl-rs@github.com";
            "nic-hdl": "RPSL1-RIPE";
            "source": "RIPE";
        },
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_multi(
                "address",
                ["Packet Street 6", "128 Series of Tubes", "Internet"],
            ),
            Attribute::unchecked_single("email", "rpsl-rs@github.com"),
            Attribute::unchecked_single("nic-hdl", "RPSL1-RIPE"),
            Attribute::unchecked_single("source", "RIPE"),
        ])
    )]
    fn object_from_macro(#[case] from_macro: Object, #[case] expected: Object) {
        assert_eq!(from_macro, expected);
    }

    #[rstest]
    #[allow(clippy::used_underscore_binding)]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_single("address", "Packet Street 6"),
        ]),
        Rfc2622
    )]
    fn object_validate_conformant_object_validates<TargetSpec: Specification>(
        #[case] object: Object,
        #[case] _target: TargetSpec,
    ) {
        object.validate::<TargetSpec>().unwrap();
    }

    #[rstest]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_single("a", "Packet Street 6"),
            Attribute::unchecked_single("1mail", "rpsl-rs@github.com"),
        ]),
        Rfc2622,
        vec![
            (
                1,
                AttributeError::from(
                    InvalidNameError::new(&Name::new("a"), "must be at least two characters long")
                ),
            ),
            (
                2,
                AttributeError::from(
                    InvalidNameError::new(&Name::new("1mail"), "must start with an ASCII alphabetic character")
                ),
            )
        ]
    )]
    #[allow(clippy::used_underscore_binding)]
    fn object_validate_invalid_object_returns_expected_errors<
        TargetSpec: Specification + PartialEq,
    >(
        #[case] object: Object,
        #[case] _target: TargetSpec,
        #[case] expected: Vec<(usize, AttributeError)>,
    ) {
        let errors = object.validate::<TargetSpec>().unwrap_err().into_errors();
        assert_eq!(errors, expected);
    }

    #[test]
    fn object_into_spec_preserves_source() {
        let source = concat!(
            "role:           ACME Company\n",
            "source:         RIPE\n",
            "\n"
        );
        let object = Object::new_parsed(
            source,
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_single("source", "RIPE"),
            ],
        );

        let converted = object.into_spec::<Rfc2622>().unwrap();
        assert_eq!(converted.source(), Some(source));
    }

    #[rstest]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("role", "ACME Company"),
            Attribute::unchecked_single("a", "Packet Street 6"),
            Attribute::unchecked_single("mail", "rpsl-rs@github.com"),
        ]),
        Rfc2622,
        AttributeError::from(
            InvalidNameError::new(&Name::new("a"), "must be at least two characters long")
        ),
    )]
    #[allow(clippy::used_underscore_binding)]
    fn object_into_spec_returns_first_validation_error<TargetSpec: Specification + PartialEq>(
        #[case] object: Object,
        #[case] _target: TargetSpec,
        #[case] expected: AttributeError,
    ) {
        let error = object.into_spec::<TargetSpec>().unwrap_err();
        assert_eq!(error, expected);
    }

    #[rstest]
    #[case(
        Object::new(vec![
            Attribute::unchecked_single("aut-num", "AS42"),
            Attribute::unchecked_single(
                "remarks",
                "All imported prefixes will be tagged with geographic communities and",
            ),
            Attribute::unchecked_single(
                "remarks",
                "the type of peering relationship according to the table below, using the default",
            ),
            Attribute::unchecked_single(
                "remarks",
                "announce rule (x=0).",
            ),
            Attribute::unchecked_single("remarks", None),
            Attribute::unchecked_single(
                "remarks",
                "The following communities can be used by peers and customers",
            ),
            Attribute::unchecked_multi(
                "remarks",
                [
                    "x = 0 - Announce (default rule)",
                    "x = 1 - Prepend x1",
                    "x = 2 - Prepend x2",
                    "x = 3 - Prepend x3",
                    "x = 9 - Do not announce",
                ],
            ),
        ]),
        vec![
            ("aut-num", vec!["AS42"]),
            (
                "remarks",
                vec![
                    "All imported prefixes will be tagged with geographic communities and",
                    "the type of peering relationship according to the table below, using the default",
                    "announce rule (x=0).",
                    "The following communities can be used by peers and customers",
                    "x = 0 - Announce (default rule)",
                    "x = 1 - Prepend x1",
                    "x = 2 - Prepend x2",
                    "x = 3 - Prepend x3",
                    "x = 9 - Do not announce",
                ]
            )
        ]
    )]
    fn get_values_by_name(#[case] object: Object, #[case] name_expected: Vec<(&str, Vec<&str>)>) {
        for (name, expected) in name_expected {
            assert_eq!(object.get(name), expected);
        }
    }

    #[rstest]
    #[case(
        Object::new(
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_single("address", "Packet Street 6"),
                Attribute::unchecked_single("address", "128 Series of Tubes"),
                Attribute::unchecked_single("address", "Internet"),
            ]),
        Object::new(
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_single("address", "Packet Street 6"),
                Attribute::unchecked_single("address", "128 Series of Tubes"),
                Attribute::unchecked_single("address", "Internet"),
            ]),
    )]
    #[case(
        Object::new_parsed(
            concat!(
                "role:           ACME Company\n",
                "address:        Packet Street 6\n",
                "address:        128 Series of Tubes\n",
                "address:        Internet\n",
                "\n"
            ),
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_single("address", "Packet Street 6"),
                Attribute::unchecked_single("address", "128 Series of Tubes"),
                Attribute::unchecked_single("address", "Internet"),
            ],
        ),
        Object::new(
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_single("address", "Packet Street 6"),
                Attribute::unchecked_single("address", "128 Series of Tubes"),
                Attribute::unchecked_single("address", "Internet"),
            ],
        ),
    )]
    /// Objects with equal attributes evaluate as equal, without taking the source field into consideration.
    fn eq_objects_are_eq(#[case] object_1: Object, #[case] object_2: Object) {
        assert_eq!(object_1, object_2);
    }

    #[rstest]
    #[case(
        Object::new(
            vec![
                Attribute::unchecked_single("role", "Umbrella Corporation"),
                Attribute::unchecked_single("address", "Paraguas Street"),
                Attribute::unchecked_single("address", "Raccoon City"),
                Attribute::unchecked_single("address", "Colorado"),
            ]),
        Object::new(
            vec![
                Attribute::unchecked_single("role", "ACME Company"),
                Attribute::unchecked_single("address", "Packet Street 6"),
                Attribute::unchecked_single("address", "128 Series of Tubes"),
                Attribute::unchecked_single("address", "Internet"),
            ]),
    )]
    /// Objects that have different attributes do not evaluate as equal.
    fn ne_objects_are_ne(#[case] object_1: Object, #[case] object_2: Object) {
        assert_ne!(object_1, object_2);
    }
}
