# How To Contribute

Thank you for considering contributing to `rpsl-rs`!
This document intends to make contribution more accessible while aligning expectations.
Please don't hesitate to open issues and PRs regardless if anything is unclear.

By contributing to `rpsl-rs`, you agree that your code will be licensed under the terms of the MIT License without any additional terms or conditions.

## Getting Started

To gain an overview of `rpsl-rs`, please read the [documentation](https://docs.rs/rpsl-rs).

## General Guidelines

- Contributions of all sizes are welcome, including single line grammar / typo fixes.
- For new features, documentation and tests are a requirement.
- Changes must pass CI. PRs with failing CI will be treated as drafts unless you explicitly ask for help.
- Simplicity is a core objective of `rpsl-rs`. Please open an issue before working on a new feature to discuss it.

## Development Environment

### Devcontainer

For users of IDEs with support for devcontainers, it's usage is recommended.

### Other

Ensure a [recent version of rustup](https://www.rust-lang.org/tools/install) is available and optionally install [`just`].

## Coding Standards

`rpsl-rs` uses [`rustfmt`](https://github.com/rust-lang/rustfmt) for uniform fomatting and [`clippy`](https://github.com/rust-lang/rust-clippy) for basic linting and enforcement of best practices. The [`just`] `lint` recipe can be used to run both.

```sh
$ just lint
cargo clippy --all-targets --all-features
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.34s
cargo fmt --all --check
...
```

In addition to basic formatting and linting, a high code coverage should be maintained. Property based tests are used to ensure the parser can deal with any kind of RPSL input. All tests need to pass before a PR can be merged.

```sh
$ just test
```

## Performance

To ensure that the parser stays performant, benchmarks are run on every PR. To execute them locally, run `cargo bench`.

[`just`]: https://github.com/casey/just
