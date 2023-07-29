#!/usr/bin/env python3

import sys

from irrd.rpsl.rpsl_objects import rpsl_object_from_text

try:
    rpsl_filepath = sys.argv[1]
except IndexError:
    sys.exit("No RPSL file provided")
with open(rpsl_filepath) as f:
    rpsl_text = f.read()

rpsl_object_from_text(rpsl_text)
