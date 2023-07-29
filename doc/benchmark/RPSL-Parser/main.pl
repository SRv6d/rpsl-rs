#!/usr/bin/env perl -w

use RPSL::Parser;
use File::Slurp;

my $rpsl_filepath=$ARGV[0];
my $rpsl_text = read_file($rpsl_filepath);

RPSL::Parser->parse( $rpsl_text );
