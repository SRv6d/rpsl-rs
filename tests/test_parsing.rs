#![allow(missing_docs)]
use proptest::prelude::*;
use rpsl::parse_object;

proptest! {
    /// Ensure RFC 2622 conformant RPSL is parsed correctly.
    #[test]
    fn rfc_2622_rpsl_parsed_to_object(
        (object, rpsl) in strategies::rfc_2622_object_w_rpsl()
    ) {
        let parsed = parse_object(&rpsl).unwrap();
        prop_assert_eq!(parsed, object);
    }
}

proptest! {
    #[test]
    fn permissive_rpsl_parsed_to_object(
        (object, rpsl) in strategies::permissive_object_w_rpsl()
    ) {
        let parsed = parse_object(&rpsl).unwrap();
        prop_assert_eq!(parsed, object);
    }
}

mod strategies {
    use std::{fmt::Write as _, ops::RangeInclusive};

    use proptest::{prelude::*, strategy::BoxedStrategy};
    use rpsl::Value;

    const CONTENT_LEN: RangeInclusive<usize> = 1..=80;

    /// An attribute name conforming to RFC 2622.
    ///
    /// According to the RFC, an "<object-name>" is made up of letters, digits, the character underscore "_",
    /// and the character hyphen "-"; the first character of a name must be a letter, and
    /// the last character of a name must be a letter or a digit.
    ///
    /// Creates a string of ASCII characters including letters, digits, underscore and hyphen,
    /// where the first character is a letter and the last character is a letter or a digit.
    fn rfc_2622_attribute_name() -> impl Strategy<Value = String> {
        proptest::string::string_regex("[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]").unwrap()
    }

    /// An attribute value conforming to RFC 2622.
    ///
    /// According to the RFC, an attribute value may consist of any ASCII characters excluding control and
    /// must not start with, or consist entirely of whitespace.
    fn rfc_2622_attribute_value_content() -> BoxedStrategy<String> {
        let ascii_range = (0x21u8..=0x7Eu8).prop_map(|b| b as char);
        prop::collection::vec(ascii_range, CONTENT_LEN)
            .prop_map(|chars| chars.into_iter().collect::<String>())
            .boxed()
    }

    /// An attribute value that can contain arbitrary Unicode scalars excluding newlines.
    fn permissive_attribute_value_content() -> BoxedStrategy<String> {
        let max_tail = CONTENT_LEN.end().saturating_sub(1);
        proptest::string::string_regex(&format!(r"[^\s][^\n]{{0,{max_tail}}}"))
            .unwrap()
            .boxed()
    }

    /// An empty attribute value.
    ///
    /// An attribute value consisting of zero or more spaces.
    fn attribute_value_empty() -> impl Strategy<Value = String> {
        proptest::string::string_regex(" {0,}").unwrap()
    }

    /// The space separator between an attribute name and its value.
    fn space_separator() -> impl Strategy<Value = String> {
        proptest::string::string_regex(" {0,20}").unwrap()
    }

    fn multiline_continuation_prefix() -> impl Strategy<Value = String> {
        prop_oneof![Just(" "), Just("\t"), Just("+")].prop_map(ToOwned::to_owned)
    }

    /// A test type that represents an attribute value.
    /// Since empty values are only coerced to `None` after parsing, the `Option` type is not used here.
    #[derive(Clone, Debug)]
    enum AttributeValue {
        Single(String),
        Multi(Vec<String>),
    }

    /// An attribute value. Either a single value or a multi-line value where value(s) may be empty.
    fn attribute_value<C>(content: C) -> BoxedStrategy<AttributeValue>
    where
        C: Strategy<Value = String> + 'static,
    {
        let value = prop_oneof![attribute_value_empty(), content].boxed();

        let single = value.clone().prop_map(AttributeValue::Single);
        let multi = proptest::collection::vec(value.clone(), 2..20).prop_map(AttributeValue::Multi);

        prop_oneof![single, multi].boxed()
    }

    /// An attribute and its corresponding RPSL representation.
    fn attribute_w_rpsl<C>(content: C) -> BoxedStrategy<(rpsl::Attribute<'static>, String)>
    where
        C: Strategy<Value = String> + 'static,
    {
        (
            rfc_2622_attribute_name(),
            space_separator(),
            multiline_continuation_prefix(),
            attribute_value(content),
        )
            .prop_map(|(name, space, cont_prefix, value)| {
                let attribute = rpsl::Attribute::new(
                    name.clone(),
                    match &value {
                        AttributeValue::Single(value) => Value::new_single(value),
                        AttributeValue::Multi(values) => Value::new_multi(values),
                    },
                );

                let mut rpsl = format!(
                    "{name}:{space}{value}",
                    value = {
                        match &value {
                            AttributeValue::Single(value) => value.to_owned(),
                            AttributeValue::Multi(values) => values[0].clone(),
                        }
                    }
                );
                if let AttributeValue::Multi(values) = &value {
                    for value in &values[1..] {
                        rpsl.push('\n');
                        if value.trim().is_empty() {
                            rpsl.push(char::from_u32(0x002B).unwrap()); // Add a "+", since entirely empty lines are not allowed in multi-line attributes.
                        } else {
                            write!(rpsl, "{cont_prefix}{space}{value}").unwrap();
                        }
                    }
                }

                (attribute, rpsl)
            })
            .boxed()
    }

    /// An object and its corresponding RPSL representation.
    fn object_w_rpsl<C>(content: C) -> BoxedStrategy<(rpsl::Object<'static>, String)>
    where
        C: Strategy<Value = String> + 'static,
    {
        prop::collection::vec(attribute_w_rpsl(content), 2..300)
            .prop_flat_map(|attrs_w_rpsl| {
                let mut attributes: Vec<rpsl::Attribute> = Vec::new();
                let mut rpsl = String::new();

                for (a, r) in attrs_w_rpsl {
                    attributes.push(a);
                    rpsl.push_str(&r);
                    rpsl.push('\n');
                }
                rpsl.push('\n');

                (Just(rpsl::Object::new(attributes)), Just(rpsl))
            })
            .boxed()
    }

    pub fn rfc_2622_object_w_rpsl() -> BoxedStrategy<(rpsl::Object<'static>, String)> {
        object_w_rpsl(rfc_2622_attribute_value_content())
    }

    pub fn permissive_object_w_rpsl() -> BoxedStrategy<(rpsl::Object<'static>, String)> {
        object_w_rpsl(permissive_attribute_value_content())
    }
}
