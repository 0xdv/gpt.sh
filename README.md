# GPT.sh

I created tiny tool to ask questions related to programming or Bash right in the terminal.
Consider it like a smart `man`.

# Installation

```bash
git clone git@github.com:0xdv/gpt.sh.git
cd gpt.sh
./install.sh
source ./venv-gpt/bin/activate # do not forget to activate the venv
```

# Usage

```bash
./gpt.py how to rename file

./gpt.py write script in python to scrape website

./gpt.py how to escape vim, please help
```

You also able to pass files to the input simply by pipe:

```bash
cat gpt.py | ./gpt.py explain this scirpt
```
