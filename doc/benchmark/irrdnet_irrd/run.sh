python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

hyperfine -N --warmup 3 "python3 main.py"
