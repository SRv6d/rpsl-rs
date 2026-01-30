<h1 align="center"><code>rpsl-rs</code></h1>
<div align="center">
  <a href="https://github.com/SRv6d/rpsl-rs/actions/workflows/test.yml">
    <img src="https://github.com/SRv6d/rpsl-rs/actions/workflows/test.yml/badge.svg?branch=main" alt="Test status" />
  </a>
  <a href="https://codecov.io/github/SRv6d/rpsl-rs">
    <img src="https://codecov.io/github/SRv6d/rpsl-rs/graph/badge.svg?token=M9F79BNTJ9" />
  </a>
  <a href="https://codspeed.io/SRv6d/rpsl-rs">
    <img src="https://img.shields.io/endpoint?url=https://codspeed.io/badge.json" alt="CodSpeed Badge" />
  </a>
  <a href="https://crates.io/crates/rpsl-rs">
    <img src="https://img.shields.io/crates/v/rpsl-rs.svg?logo=rust" alt="Cargo version" />
  </a>
  <a href="https://rust-lang.github.io/rfcs/2495-min-rust-version.html">
    <img src="https://img.shields.io/badge/rustc-1.80+-blue?logo=rust" alt="Rust version" />
  </a>
</div>
<div align="center">
  <a href="https://scorecard.dev/viewer/?uri=github.com/SRv6d/rpsl-rs">
    <img src="https://api.scorecard.dev/projects/github.com/SRv6d/rpsl-rs/badge" />
  </a>
  <a href="https://www.bestpractices.dev/projects/9525">
    <img src="https://www.bestpractices.dev/projects/9525/badge" />
  </a>
  <br />
</div>

A Routing Policy Specification Language (RPSL) parser with a focus on speed and correctness.

⚡️ 130-250x faster than other parsers\
📰 Complete implementation for multiline RPSL values\
💬 Able to parse objects directly from whois server responses\
🧠 Low memory footprint by leveraging zero-copy\
🧪 Robust parsing of any valid input ensured by Property Based Tests\
🧩 Optional validation via customizable specifications

[<img src="docs/benchmark/graph.svg">](docs/benchmark)

### [**Docs**](https://docs.rs/rpsl-rs/latest/rpsl/) | [**Performance**](https://github.com/SRv6d/rpsl-rs/tree/main/docs/benchmark)

## MSRV Policy

This project requires the minimum supported Rust version to be at least 6 months old.
As long as this requirement is met, the MSRV may be increased as necessary through a minor version update.
For the currently configured MSRV, please check [Cargo.toml](Cargo.toml).

## Contributing

Contributions of all sizes that improve `rpsl-rs` in any way, be it DX/UX, documentation, performance or other are highly appreciated.
To get started, please read the [contribution guidelines](.github/CONTRIBUTING.md). Before starting work on a new feature you would like to contribute that may impact simplicity, reliability or performance, please open an issue first.

## License

The source code of this project is licensed under the MIT License. For more information, see [LICENSE](LICENSE).
