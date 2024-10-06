export NEEDRESTART_MODE=a
export DEBIAN_FRONTEND=noninteractive
sudo apt update && sudo apt install -y build-essential
cargo install --locked hyperfine

sudo PERL_MM_USE_DEFAULT=1 cpan App::cpanminus
sudo cpanm RPSL::Parser

hyperfine -N --warmup 3 "perl -w main.pl"
