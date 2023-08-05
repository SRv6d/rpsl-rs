sudo PERL_MM_USE_DEFAULT=1 cpan App::cpanminus
sudo cpanm RPSL::Parser

hyperfine -N --warmup 3 "perl -w main.pl"
