# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- This Changelog.

## [1.0.1] - 2024-12-26

### Added

- Rust MSRV.
- Contribution guidelines.

## 1.0.0 - 2023-12-26

### Added

- Validation that newly created attribute names start with alphabetic and end with alphanumeric characters.
- CI benchmarks using codspeed.
- Distinct types for multi line / multi value RPSL values.
- Improved conversion traits.
- Property based testing of the parser using proptest.
- Improvement of parsing speed by 38%.
- `object!` macro to simplify object creation.

### Changed

- Parse RPSL into types containing string references instead of making assignments for each attribute.
- Simplified functions exposed by the API.
- Crate name to rpsl-rs

### Removed

- Python bindings to allow for decoupled development in separate repository.

### Internal

- Complete refactor

[unreleased]: https://github.com/SRv6d/rpsl-rs/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/SRv6d/rpsl-rs/compare/v1.0.0...v1.0.1