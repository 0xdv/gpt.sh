# GPT.sh

`GPT.sh` is a command-line tool that allows you to ask programming or Bash-related questions right in the terminal.
It functions as a smart `man` page, providing answers and guidance for various programming tasks.
You can use it to ask questions about topics like Python scripting, Vim commands, and more, it's up to you.
The tool leverages the power of OpenAI's GPT language model to generate responses to your queries.

This tool doesn't have access to your file system, and won't run any commands on your computer.

# Installation

```bash
git clone git@github.com:0xdv/gpt.sh.git
cd gpt.sh
./install.sh
source ./venv-gpt/bin/activate # do not forget to activate the venv
```

# Usage

```bash
./gpt how to rename file

./gpt write script in python to scrape website

./gpt how to escape vim, please help
```

You also able to pass files to the input simply by pipe:

```bash
cat install.sh | ./gpt explain this scirpt
```

- remember DO NOT pass any confidential data to the input
