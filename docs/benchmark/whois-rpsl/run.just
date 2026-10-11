RIPE_WHOIS_REPOSITORY_URL := "https://github.com/RIPE-NCC/whois.git"
RIPE_WHOIS_RELEASE := "1a68e9a8"

bench-whois-rpsl: _install_hyperfine
    #!/usr/bin/env bash
    set -euxo pipefail

    sudo apt update
    sudo apt install -y build-essential openjdk-21-jdk maven

    WHOIS_SOURCE="target/benchmark/RIPE-NCC-whois-{{ RIPE_WHOIS_RELEASE }}"
    MAVEN_REPOSITORY="target/benchmark/maven-repository"
    if [[ ! -d "$WHOIS_SOURCE" ]]; then
        git clone --depth 1 --branch "{{ RIPE_WHOIS_RELEASE }}" "{{ RIPE_WHOIS_REPOSITORY_URL }}" "$WHOIS_SOURCE"
    fi

    mvn -q -f "$WHOIS_SOURCE/pom.xml" -pl whois-rpsl -am install -Dmaven.test.skip=true -Dmaven.repo.local="$MAVEN_REPOSITORY"
    mvn -q -f docs/benchmark/whois-rpsl/pom.xml package -Dmaven.repo.local="$MAVEN_REPOSITORY"

    hyperfine -N --warmup 3 "java -jar docs/benchmark/whois-rpsl/target/parser-test-0.1.0.jar docs/benchmark/whois-rpsl/AS3257.txt"
