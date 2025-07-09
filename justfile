import "docs/benchmark/benchmark.just"

export CI := env("CI", "false")
CHANGELOG_FILE := "CHANGELOG.md"
REPO_URL := "https://github.com/SRv6d/rpsl-rs"

default: check-lockfile lint test

# Check if the lockfile is up to date
check-lockfile:
    cargo update -w --locked

# Lint code and check formatting
lint: lint-justfile
    cargo clippy --all-targets --all-features
    cargo fmt --all --check

lint-justfile:
    just --check --fmt --unstable

cov_output := if CI == "true" { "--lcov --output-path lcov.info" } else { "--summary-only" }

# Run tests
test $COV=CI: (_install_llvm_cov COV) && doc-test
    {{ if COV == "true" { "cargo llvm-cov --all-features" + " " + cov_output } else { "cargo test --lib --all-features" } }}

# Run documentation and example tests
doc-test:
    cargo test --all-features --doc
    cargo test --all-features --examples

# Alias to run tests with coverage
coverage: (test "true")

# Check feature combinations
check-features:
    cargo hack check --each-feature --no-dev-deps

# Bump our version
bump-version $VERSION: _check_clean_working (_validate_semver VERSION) && (_changelog_add_version VERSION) (_bump_version_pr VERSION)
    #!/usr/bin/env bash
    set -euxo pipefail

    sed -i 's/^version = .*/version = "'$VERSION'"/g' Cargo.toml
    cargo update -w --offline

    git add Cargo.toml Cargo.lock
    git commit -m "Bump version to v{{ VERSION }}"

# Create a GitHub release containing the latest changes
release-latest-version version:
    #!/usr/bin/env bash
    set -euxo pipefail
    PREVIOUS_RELEASE=$(gh release list --json name,isLatest --jq '.[] | select(.isLatest)|.name')
    CURRENT_RELEASE="v{{ version }}"
    CHANGES=$(sed -n "/^## \[{{ version }}]/,/^## \[[0-9].*\]/ {//!p}" {{ CHANGELOG_FILE }})
    RELEASE_NOTES="
    ## What's Changed

    $CHANGES

    **Full Changelog**: {{ REPO_URL }}/compare/$PREVIOUS_RELEASE...$CURRENT_RELEASE
    "

    gh release create $CURRENT_RELEASE --latest --title $CURRENT_RELEASE --notes-file - <<< "$RELEASE_NOTES"

# Publish the crate
publish: _validate_version_tag
    cargo publish --no-verify

# Check that Git has a clean working directory
_check_clean_working:
    test -z "$(git status --porcelain)" || (echo "The working directory is not clean"; exit 1)

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

_install_llvm_cov $run:
    #!/usr/bin/env bash
    set -euxo pipefail

    if [ $run == true ] && [ $CI = false ]; then
        cargo install cargo-llvm-cov --locked
    fi

# Update the changelog with a new version
_changelog_add_version version filename=CHANGELOG_FILE:
    #!/usr/bin/env bash
    set -euxo pipefail
    PREV_VERSION=$(sed -n "/^\[unreleased\]:/ { n; s/^\[\([^]]*\)\].*/\1/p }" {{ filename }})

    sed -i "/^## \[Unreleased\]$/ { N; s/\n/\n\n## [{{ version }}] - {{ datetime('%Y-%m-%d') }}\n/ }" {{ filename }}
    sed -i "/^\[unreleased\]:/ s/v[0-9.]\+\b/v{{ version }}.../; /^\[unreleased\]:/ a\
    [{{ version }}]: {{ REPO_URL }}/compare/v$PREV_VERSION...v{{ version }}" {{ filename }}

    git add {{ filename }}
    git commit -m "Update {{ filename }}"

_bump_version_pr version:
    gh pr create --title "Bump version to v{{ version }}" --body ""
