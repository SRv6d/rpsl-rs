export PARSER_VERSION := "0.04000"

bench-RPSL-Parser: _install_hyperfine
    #!/usr/bin/env bash
    set -euxo pipefail

    sudo PERL_MM_USE_DEFAULT=1 cpan App::cpanminus
    sudo cpanm RPSL::Parser@$PARSER_VERSION

    hyperfine -N --warmup 3 "perl -w docs/benchmark/RPSL-Parser/main.pl"
