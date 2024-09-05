use proptest::prelude::*;
use rpsl::parse_object;

proptest! {
    /// Property based test to ensure any kind of valid RPSL is parsed correctly.
    #[test]
    fn rpsl_parsed_to_object((object, rpsl) in strategies::object_w_rpsl()) {
        let parsed = parse_object(&rpsl).unwrap();
        prop_assert_eq!(parsed, object);
    }
}

mod strategies {
    use proptest::prelude::*;

    /// A valid attribute name.
    ///
    /// According to RFC 2622, an "<object-name>" is made up of letters, digits, the character underscore "_",
    /// and the character hyphen "-"; the first character of a name must be a letter, and
    /// the last character of a name must be a letter or a digit.
    ///
    /// Creates a string of ASCII characters including letters, digits, underscore and hyphen,
    /// where the first character is a letter and the last character is a letter or a digit.
    fn attribute_name() -> impl Strategy<Value = String> {
        proptest::string::string_regex("[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]").unwrap()
    }

    /// A valid attribute value.
    ///
    /// An attribute value may consist of any ASCII characters excluding control and
    /// must not start with, or consist entirely of whitespace.
    fn attribute_value_content() -> impl Strategy<Value = String> {
        proptest::string::string_regex("[!-~][ -~]*").unwrap()
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
        prop_oneof![Just(" "), Just("\t"), Just("+")].prop_map(|s| s.to_owned())
    }

    /// A test type that represents an attribute value.
    /// Since empty values are only coerced to `None` after parsing, the `Option` type is not used here.
    #[derive(Clone, Debug)]
    enum AttributeValue {
        Single(String),
        Multi(Vec<String>),
    }

    /// An attribute value. Either a single value or a multi-line value where value(s) may be empty.
    fn attribute_value() -> impl Strategy<Value = AttributeValue> {
        prop_oneof![
            prop_oneof![attribute_value_empty(), attribute_value_content()]
                .prop_map(AttributeValue::Single),
            proptest::collection::vec(
                prop_oneof![attribute_value_empty(), attribute_value_content()],
                2..20
            )
            .prop_map(AttributeValue::Multi)
        ]
    }

    /// An attribute and its corresponding RPSL representation.
    fn attribute_w_rpsl() -> impl Strategy<Value = (rpsl::Attribute<'static>, String)> {
        (
            attribute_name(),
            space_separator(),
            multiline_continuation_prefix(),
            attribute_value(),
        )
            .prop_map(|(name, space, cont_prefix, value)| {
                let attribute = rpsl::Attribute::new(
                    name.parse().unwrap(),
                    match &value {
                        AttributeValue::Single(value) => value.parse().unwrap(),
                        AttributeValue::Multi(values) => values
                            .iter()
                            .map(AsRef::as_ref)
                            .collect::<Vec<&str>>()
                            .try_into()
                            .unwrap(),
                    },
                );

                let mut rpsl = format!(
                    "{name}:{space}{value}",
                    value = {
                        match &value {
                            AttributeValue::Single(value) => value.to_owned(),
                            AttributeValue::Multi(values) => values[0].to_owned(),
                        }
                    }
                );
                if let AttributeValue::Multi(values) = &value {
                    for value in &values[1..] {
                        rpsl.push('\n');
                        if value.trim().is_empty() {
                            rpsl.push(char::from_u32(0x002B).unwrap()); // Add a "+", since entirely empty lines are not allowed in multi-line attributes.
                        } else {
                            rpsl.push_str(&format!("{}{}{}", cont_prefix, space, value));
                        }
                    }
                }

                (attribute, rpsl)
            })
    }

    /// An object and its corresponding RPSL representation.
    pub fn object_w_rpsl() -> impl Strategy<Value = (rpsl::Object<'static>, String)> {
        prop::collection::vec(attribute_w_rpsl(), 2..300).prop_flat_map(|attrs_w_rpsl| {
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
    }
}
