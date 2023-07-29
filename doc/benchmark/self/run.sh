cargo build --release --bin benchmark --target-dir .

hyperfine -N --warmup 3 "release/benchmark ../assets/AS3257.txt"
