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
🧪 Robust parsing of any valid input ensured by Property Based Tests

> [!WARNING]
> This project is still in early stages of development and its API is not yet stable.

## Usage

### Parsing RPSL objects

A string containing an object in RPSL notation can be parsed to an [Object] using the [parse_object] function.

```rust,ignore
use rpsl_parser::parse_object;

let role_acme = "
role:        ACME Company
address:     Packet Street 6
address:     128 Series of Tubes
address:     Internet
email:       rpsl-parser@github.com
nic-hdl:     RPSL1-RIPE
source:      RIPE

";
let parsed = parse_object(role_acme)?;
```

This returns an [Object] consisting of multiple [Attribute]s:

```rust,ignore
println!("{:#?}", parsed);

Object(
  [
    Attribute {
      name: Name("role"),
      value: SingleLine(Some("ACME Company")),
    },
    Attribute {
      name: Name("address"),
      value: SingleLine(Some("Packet Street 6")),
    },
    Attribute {
      name: Name("address"),
      value: SingleLine(Some("128 Series of Tubes")),
    },
    Attribute {
      name: Name("address"),
      value: SingleLine(Some("Internet")),
    },
    Attribute {
      name: Name("email"),
      value: SingleLine(Some("rpsl-parser@github.com")),
    },
    Attribute {
      name: Name("nic-hdl"),
      value: SingleLine(Some("RPSL1-RIPE")),
    },
    Attribute {
      name: Name("source"),
      value: SingleLine(Some("RIPE")),
    },
  ],
)
```

Each [Attribute] can be accessed by it's index and has a name and optional value(s).

```rust,ignore
println!("{:#?}", parsed[1]);

Attribute {
    name: Name("role"),
    value: SingleLine(Some("ACME Company")),
}
```

Since RPSL attribute values can either be single- or multiline, two different types are used to represent them. See [Attribute] and [parse_object] for more details and examples.

### Parsing a WHOIS server response

WHOIS servers often respond to queries by returning multiple related objects.
An example ARIN query for `AS32934` will return with the requested `ASNumber` object first, followed by it's associated `OrgName`:

```sh
$ whois -h whois.arin.net AS32934
ASNumber:       32934
ASName:         FACEBOOK
ASHandle:       AS32934
RegDate:        2004-08-24
Updated:        2012-02-24
Comment:        Please send abuse reports to abuse@facebook.com
Ref:            https://rdap.arin.net/registry/autnum/32934


OrgName:        Facebook, Inc.
OrgId:          THEFA-3
Address:        1601 Willow Rd.
City:           Menlo Park
StateProv:      CA
PostalCode:     94025
Country:        US
RegDate:        2004-08-11
Updated:        2012-04-17
Ref:            https://rdap.arin.net/registry/entity/THEFA-3


```

To extract each individual object, the [parse_whois_response] function can be used to parse the response into a `Vec` containing all individual [Object]s within the response. Examples can be found in the function documentation.

# 🚧 Work in progress

- ## More descriptive error messages
  When invalid RPSL is parsed, the current error messages do not properly convey where exactly the error is located in the parsed text.

[RFC 2622]: https://datatracker.ietf.org/doc/html/rfc2622
[Object]: https://docs.rs/rpsl-parser/latest/rpsl_parser/struct.Object.html
[Attribute]: https://docs.rs/rpsl-parser/latest/rpsl_parser/struct.Attribute.html
[parse_object]: https://docs.rs/rpsl-parser/latest/rpsl_parser/fn.parse_object.html
[parse_whois_server_response]: https://docs.rs/rpsl-parser/latest/rpsl_parser/fn.parse_whois_response.html
