bench-whois-rpsl: _install_hyperfine
    #!/usr/bin/env bash
    set -euxo pipefail

    sudo apt update && sudo apt install -y build-essential openjdk-18-jre openjdk-18-jdk maven
    
    cd docs/benchmark/whois-rpsl

    mvn package

    hyperfine -N --warmup 3 "java -jar target/parser-test-0.1.0.jar ./AS3257.txt"
