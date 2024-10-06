export PYTHON_VERSION := "3.11"
export IRRD_VERSION := "4.4.2"

bench-irrdnet_irrd: _install_uv _install_hyperfine
    #!/usr/bin/env bash
    set -euxo pipefail

    uv venv --python $PYTHON_VERSION
    source .venv/bin/activate
    uv pip install irrd==$IRRD_VERSION

    hyperfine -N --warmup 3 "python3 docs/benchmark/irrdnet_irrd/main.py"

    rm -rf .venv

_install_uv:
    curl -LsSf https://astral.sh/uv/install.sh | sh
