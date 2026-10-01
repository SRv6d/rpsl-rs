package parser;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

import net.ripe.db.whois.common.rpsl.RpslObject;

public final class TestParser {
    private TestParser() {}

    public static void main(final String[] arguments) throws IOException {
        if (arguments.length != 1) {
            throw new IllegalArgumentException("usage: TestParser RPSL_OBJECT");
        }

        RpslObject.parse(Files.readString(Path.of(arguments[0])));
    }
}
