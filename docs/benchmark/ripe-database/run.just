RIPE_DATABASE_MANIFEST := "docs/benchmark/ripe-database/rpsl-rs/Cargo.toml"
RIPE_DATABASE_CACHE := "target/benchmark/ripe-database"
RIPE_DATABASE_FILE := RIPE_DATABASE_CACHE / "ripe.db.utf8"
RIPE_DATABASE_ADAPTER := "docs/benchmark/ripe-database/rpsl-rs/target/release/parse-ripe-database-rpsl-rs"

prepare-ripe-database:
    cargo run --release --manifest-path {{ RIPE_DATABASE_MANIFEST }} --bin prepare-ripe-database -- {{ RIPE_DATABASE_CACHE }}

bench-ripe-database-rpsl-rs: _install_hyperfine prepare-ripe-database
    cargo build --release --manifest-path {{ RIPE_DATABASE_MANIFEST }} --bin parse-ripe-database-rpsl-rs
    hyperfine -N --warmup 3 "{{ RIPE_DATABASE_ADAPTER }} {{ RIPE_DATABASE_FILE }}"

benchmark-ripe-database: bench-ripe-database-rpsl-rs
