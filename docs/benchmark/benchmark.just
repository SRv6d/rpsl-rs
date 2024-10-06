import "irrdnet_irrd/run.just"
import "RPSL-Parser/run.just"
import "whois-rpsl/run.just"

benchmark-comparison: bench-irrdnet_irrd bench-RPSL-Parser bench-whois-rpsl

_install_hyperfine:
    cargo install --locked hyperfine
