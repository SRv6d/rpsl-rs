# benchmark

Benchmarks comparing performance to other RPSL parsers.

## Results

| Parser            | Mean              | Min       | Max       |
| ----------------- | ----------------- | --------- | --------- |
| **[rpsl-parser]** | 1.86 ms           | 1.8642 ms | 1.8693 ms |
| [RPSL::Parser]    | 61.8 ms ± 2.5 ms  | 60.1 ms   | 74.7 ms   |
| [irrdnet/irrd]    | 98.6 ms ± 3.4 ms  | 91.2 ms   | 110.9 ms  |
| [RIPE-NCC/whois]  | 114.7 ms ± 6.3 ms | 106.5 ms  | 124.6 ms  |

_Parsing of the AS3257 aut-num object on a 2022 M1 Max._

## Methology

For each benchmarked parser, a small executable is created in its native language that parses the AS3257 aut-num object.
With the exception of [RIPE-NCC/whois], the AS3257 object is included as a string literal. To benchmark [RIPE-NCC/whois], the AS3257 object has to be read from a file since Java limits the length of string literals.

## Running Benchmarks

`./run` in the directory of the specific parser sets up dependencies and runs a benchmark using [hyperfine]. It runs `sudo` and is only guaranteed to run correctly within the [benchmark workflow](https://github.com/SRv6d/rpsl-parser/blob/main/.github/workflows/benchmark.yml), which can be used as a reference for additionally required dependencies.

[rpsl-parser]: https://github.com/srv6d/rpsl-parser
[RPSL::Parser]: https://metacpan.org/pod/RPSL::Parser
[irrdnet/irrd]: https://github.com/irrdnet/irrd
[RIPE-NCC/whois]: https://github.com/RIPE-NCC/whois
[hyperfine]: https://github.com/sharkdp/hyperfine
