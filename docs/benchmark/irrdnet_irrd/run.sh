export NEEDRESTART_MODE=a
export DEBIAN_FRONTEND=noninteractive
sudo apt update && sudo apt install -y build-essential python3-venv python3-pip
cargo install --locked hyperfine

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

hyperfine -N --warmup 3 "python3 main.py"
