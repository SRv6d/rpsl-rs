CI := env("CI", "false")

default: lint test

# Lint code and check formatting
lint: lint-justfile
    cargo clippy --all-targets --all-features
    cargo fmt --all --check

lint-justfile:
    just --check --fmt --unstable

cov_output := if CI == "true" { "--lcov" } else { "--summary-only" }

# Run tests
test $COV=CI:
    {{ if COV == "true" { "cargo llvm-cov --all-features" + " " + cov_output } else { "cargo test --all-features" } }}

# Bump our version
bump-version $VERSION: (_validate_semver VERSION)
    #!/usr/bin/env bash
    set -euxo pipefail

    test -z "$(git status --porcelain)" || (echo "The working directory is not clean"; exit 1)

    sed -i 's/^version = .*/version = "'$VERSION'"/g' Cargo.toml

    git add Cargo.toml
    git commit -m "Bump version to v{{ VERSION }}"

# Publish the crate
publish: _validate_version_tag
    cargo publish --no-verify

# Validate that the crate version matches that of the git tag
_validate_version_tag:
    #!/usr/bin/env bash
    set -euxo pipefail
    PROJECT_VERSION="$(grep -Po '(?<=^version = ").*(?=")' Cargo.toml)"
    GIT_TAG="$(git describe --exact-match --tags)"

    if [ ! $PROJECT_VERSION == ${GIT_TAG:1} ]; then
        echo Project version $PROJECT_VERSION does not match git tag $GIT_TAG
        exit 1
    fi

# Validate a version against SemVer
_validate_semver version:
    #!/usr/bin/env bash
    set -euxo pipefail
    if [[ ! "{{ version }}" =~ ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(-((0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*))*))?(\+([0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*))?$ ]]; then
        echo Invalid SemVer {{ version }}
        exit 1
    fi
