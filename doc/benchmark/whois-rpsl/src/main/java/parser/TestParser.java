package parser;

import java.util.Set;
import java.util.HashSet;
import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;

import net.ripe.db.whois.common.io.RpslObjectStringReader;
import net.ripe.db.whois.common.rpsl.RpslObject;

public class TestParser {
	public static void main(String[] args)
		throws IOException
	 {
		Path RpslFilepath = Path.of(args[0]);
		String RPSL = Files.readString(RpslFilepath); 

		RpslObjectStringReader reader = new RpslObjectStringReader(RPSL);
		for(String objectString : reader)
			RpslObject.parse(objectString);
	}
}
