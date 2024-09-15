default: lint test

# Lint code and check formatting
lint: lint-justfile
    cargo clippy --all-targets --all-features
    cargo fmt --all --check

lint-justfile:
    just --check --fmt --unstable

# Run tests
test:
    cargo test --all-features

# Bump our version
bump-version $VERSION: (_validate_semver VERSION)
    #!/usr/bin/env bash
    set -euxo pipefail

    test -z "$(git status --porcelain)" || (echo "The working directory is not clean"; exit 1)

    sed -i 's/^version = .*/version = "'$VERSION'"/g' Cargo.toml

    git add Cargo.toml
    git commit -m "Bump version to v{{ VERSION }}"

# Validate a version against SemVer
_validate_semver version:
    #!/usr/bin/env bash
    set -euxo pipefail
    if [[ ! "{{ version }}" =~ ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(-((0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*))*))?(\+([0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*))?$ ]]; then
        echo Invalid SemVer {{ version }}
        exit 1
    fi
