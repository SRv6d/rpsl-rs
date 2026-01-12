# benchmark

Benchmarks comparing performance to other RPSL parsers.

## Results

![graph](graph.svg)

| Parser           | Mean              | Min       | Max       | Compiler / Runtime                              |
| ---------------- | ----------------- | --------- | --------- | ----------------------------------------------- |
| **rpsl-rs**      | **454.98 µs**     | 454.76 µs | 455.22 µs | rustc 1.92.0 (ded5c06cf 2025-12-08) LLVM 21.1.3 |
| [RPSL::Parser]   | 59.4 ms ± 3.2 ms  | 58.1 ms   | 81.3 ms   | perl v5.36.0                                    |
| [irrdnet/irrd]   | 93.5 ms ± 2.5 ms  | 90.7 ms   | 102.4 ms  | Python 3.11.2                                   |
| [RIPE-NCC/whois] | 114.7 ms ± 6.3 ms | 106.5 ms  | 124.6 ms  | openjdk version "17.0.12" 2024-07-16            |

_Parsing of the AS3257 aut-num object on a 2022 M1 Max running macOS 15.0 (24A335)._

## Methology

For each benchmarked parser, a small executable is created in its native language that parses the AS3257 aut-num object.
With the exception of [RIPE-NCC/whois], the AS3257 object is included as a string literal. To benchmark [RIPE-NCC/whois], the AS3257 object has to be read from a file since Java limits the length of string literals.

## Running Benchmarks

Benchmarks for the parser itself are done using `cargo bench`, while any external parser is benchmarked using [hyperfine].\
To run a specific benchmark execute `just bench-$PARSER-NAME` or `just benchmark-comparison` to run all benchmarks. This will setup required dependencies and run `sudo` so it is only recommended to be used in an isolated environment and is only tested using the devcontainer, other platforms might require additional dependencies to be installed. A working installation of `just` and `cargo` is assumed.

[RPSL::Parser]: https://metacpan.org/pod/RPSL::Parser
[irrdnet/irrd]: https://github.com/irrdnet/irrd
[RIPE-NCC/whois]: https://github.com/RIPE-NCC/whois
[hyperfine]: https://github.com/sharkdp/hyperfine
