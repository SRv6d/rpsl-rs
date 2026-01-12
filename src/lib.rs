//! A Routing Policy Specification Language (RPSL) parser with a focus on speed and correctness.
//!
//! ⚡️ 130-250x faster than other parsers\
//! 📰 Complete implementation for multiline RPSL values\
//! 💬 Able to parse objects directly from whois server responses\
//! 🧠 Low memory footprint by leveraging zero-copy\
//! 🧪 Robust parsing of any valid input ensured by Property Based Tests\
//! 🧩 Optional validation via customizable specifications
//!
//! ## Usage
//!
//! ### Parsing RPSL objects
//!
//! A string containing an object in RPSL notation can be parsed using the [`parse_object`] function.
//!
//! ```rust
//! use rpsl::{parse_object, Object, spec::Raw};
//!
//! let role_acme = "
//! role:        ACME Company
//! address:     Packet Street 6
//! address:     128 Series of Tubes
//! address:     Internet
//! email:       rpsl-rs@github.com
//! nic-hdl:     RPSL1-RIPE
//! source:      RIPE
//!
//! ";
//! let parsed: Object<Raw> = parse_object(role_acme)?;
//! # Ok::<(), Box<dyn std::error::Error>>(())
//! ```
//!
//! This returns an [`Object<Raw>`], a sorted [`Attribute<Raw>`] collection which contain string references
//! pointing to attributes and their values from the parsed text.
//!
//! ```text
//! role:           ACME Company ◀─────────────── &"role":      &"ACME Company"
//! address:        Packet Street 6 ◀──────────── &"address":   &"Packet Street 6"
//! address:        128 Series of Tubes ◀──────── &"address":   &"128 Series of Tubes"
//! address:        Internet ◀─────────────────── &"address":   &"Internet"
//! email:          rpsl-rs@github.com ◀───────── &"email":     &"rpsl-rs@github.com"
//! nic-hdl:        RPSL1-RIPE ◀───────────────── &"nic-hdl":   &"RPSL1-RIPE"
//! source:         RIPE ◀─────────────────────── &"source":    &"RIPE"
//! ```
//!
//! Parsing is intentionally lenient and returns objects typed with [`Raw`](spec::Raw), meaning no
//! validation has been applied. To ensure the object conforms to a [`Specification`](spec::Specification),
//! it can be converted to a typed spec after parsing.
//!
//! ```rust
//! # use rpsl::{parse_object, Object, spec::Rfc2622};
//! # let parsed = parse_object("role: ACME Company\nsource: RIPE\n\n")?;
//! let validated: Object<Rfc2622> = parsed.into_spec()?;
//! # Ok::<(), Box<dyn std::error::Error>>(())
//! ```
//!
//! For more information on object validation, see the [`spec`] module.
//!
//! ### Parsing a WHOIS server response
//!
//! WHOIS servers often respond to queries by returning multiple related objects.
//! An example ARIN query for `AS32934` will return with the requested `ASNumber` object first, followed by its associated `OrgName`:
//!
//! ```sh
//! $ whois -h whois.arin.net AS32934
//! ASNumber:       32934
//! ASName:         FACEBOOK
//! ASHandle:       AS32934
//! RegDate:        2004-08-24
//! Updated:        2012-02-24
//! Comment:        Please send abuse reports to abuse@facebook.com
//! Ref:            https://rdap.arin.net/registry/autnum/32934
//!
//!
//! OrgName:        Facebook, Inc.
//! OrgId:          THEFA-3
//! Address:        1601 Willow Rd.
//! City:           Menlo Park
//! StateProv:      CA
//! PostalCode:     94025
//! Country:        US
//! RegDate:        2004-08-11
//! Updated:        2012-04-17
//! Ref:            https://rdap.arin.net/registry/entity/THEFA-3
//!
//!
//! ```
//!
//! To extract each individual object, the [`parse_whois_response`] function can be used to parse the response into a [`Vec`] containing all individual [`Object`]s within the response. Examples can be found in the function documentation.
//!
//! ## Optional Features
//!
//! The following cargo features can be used to enable additional functionality.
//!
//! - **simd** _(enabled by default)_: Enables the [Winnow](https://github.com/winnow-rs/winnow) simd feature which improves string search performance using simd.
//! - **serde**: Enables [Object] serialization using [Serde](https://github.com/serde-rs/serde).
//! - **json**: Provides JSON serialization of an [Object] using [Serde JSON](https://github.com/serde-rs/json).
#![cfg_attr(docsrs, feature(doc_cfg))]

pub use attribute::{Attribute, Name, Value};
pub use object::Object;
pub use parser::{parse_object, parse_whois_response, ParseError};

mod attribute;
mod object;
mod parser;
pub mod spec;
