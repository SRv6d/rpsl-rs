mvn package

hyperfine -N --warmup 3 "java -jar target/parser-test-0.1.0.jar ../assets/AS3257.txt"