<h1 align="center"><code>rpsl-parser</code></h1>

<div align="center">
  <a href="https://github.com/srv6d/rpsl-parser/actions">
    <img src="https://github.com/srv6d/rpsl-parser/workflows/CI/badge.svg" alt="CI status">
  </a>
  <a href="https://crates.io/crates/rpsl-parser">
    <img src="https://img.shields.io/crates/v/rpsl-parser.svg" alt="Cargo version">
  </a>
  
</div>
<br>

An [RFC 2622] conformant Routing Policy Specification Language (RPSL) parser with a focus on speed and correctness.

⚡️ Outperforms other parsers by a factor of 33-60x\
📰 Complete implementation for multiline RPSL values\
💬 Able to parse objects directly from whois server responses\
🧠 Low memory footprint by leveraging zero-copy\
🧪 Robust parsing of any valid input ensured by Property Based Tests\
🐍 Python usage is supported

> [!WARNING]
> This project is still in early stages of development and its API is not yet stable.

## Examples

### Parsing RPSL

A string containing an object in RPSL notation can be parsed to a [rpsl::Object] struct using the [parse_rpsl_object] function.

```rust
let role_acme = "
role:        ACME Company
address:     Packet Street 6
address:     128 Series of Tubes
address:     Internet
email:       rpsl-parser@github.com
nic-hdl:     RPSL1-RIPE
source:      RIPE
";
let parsed = rpsl_parser::parse_rpsl_object(role_acme).unwrap();
```

This returns an [rpsl::Object] consiting of multiple [rpsl::Attribute]s:

```rust
println!("{:#?}", parsed);

Object(
  [
    Attribute {
      name: "role",
      values: [Some("ACME Company",),],
    },
    Attribute {
      name: "address",
      values: [Some("Packet Street 6",),],
    },
    Attribute {
      name: "address",
      values: [Some("128 Series of Tubes",),],
    },
    Attribute {
      name: "address",
      values: [Some("Internet",),],
    },
    Attribute {
      name: "email",
      values: [Some("irrdb@github.com",),],
    },
    Attribute {
      name: "nic-hdl",
      values: [Some("IRRD2-RIPE",),],
    },
    Attribute {
      name: "source",
      values: [Some("RIPE",),],
    },
  ],
)
```

Each [rpsl::Attribute] can be accessed by it's index and has a name and an optional set of values.

```rust
println!("{:#?}", parsed.1);

Attribute {
    name: "role",
    values: [Some("ACME Company",),],
}
```

Because RPSL attribute values may be spread over multiple lines and values consisting only of whitespace are valid, the `Vec<Option<String>>` type is used to represent them.

Thus, an object with a single attribute with values spread over multiple lines is represented as such:

```rust
let multi_value = "
remarks:     Value 1
             Value 2
";
assert_eq!(
    parse_rpsl_object(multi_value).unwrap(),
    rpsl::Object::new(vec![rpsl::Attribute::new(
        "remarks".to_string(),
        vec![Some("Value 1".to_string()), Some("Value 2".to_string())]
    ),])
);
```

And an object with a remark consisting only of whitespace separating two attributes:

```rust
let whitespace_value = "
as-name:     REMARKABLE
remarks:               
remarks:     ^^^^^^^^^^ nothing but hot air
";
assert_eq!(
    parse_rpsl_object(whitespace_value).unwrap(),
    rpsl::Object::new(vec![
        rpsl::Attribute::new("as-name".to_string(), vec![Some("REMARKABLE".to_string())]),
        rpsl::Attribute::new("as-name".to_string(), vec![None]),
        rpsl::Attribute::new(
            "as-name".to_string(),
            vec![Some("^^^^^^^^^^ nothing but hot air".to_string())]
        ),
    ])
);
```

# Python bindings

To use this parser in Python, see the [rpsl-parser PyPi Package](https://pypi.org/project/rpsl-parser/).

[RFC 2622]: https://datatracker.ietf.org/doc/html/rfc2622
[rpsl::Object]: https://docs.rs/rpsl-parser/latest/rpsl_parser/rpsl/struct.Object.html
[rpsl::Attribute]: https://docs.rs/rpsl-parser/latest/rpsl_parser/rpsl/struct.Attribute.html
[parse_rpsl_object]: https://docs.rs/rpsl-parser/latest/rpsl_parser/fn.parse_rpsl_object.html
