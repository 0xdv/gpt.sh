#!/usr/bin/env python

import sys
import g4f
from termcolor import colored
from rich.console import Console
from rich.markdown import Markdown
import time

g4f.debug.version_check = False

console = Console()

def generate_response(prompt: str) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo_16k_0613,
        messages=[{"role": "user", "content": prompt}],
    )
    return response

prompt = """
    Imagine you are an expert Linux, Bash scripting, JavaScript, Python and related fields.
    I will ask you questions related this area and expect for your help.
    Please answer as short as possible, do not include unneeded details to your answer.
    Omit surplus unnecessary text, concentrate on code examples.
"""

if not sys.stdin.isatty():
    file =  "".join([line for line in sys.stdin])
    prompt += f"""
        I have file:
        {file}

    """

user_input = ' '.join(sys.argv[1:])

prompt += f"""
My question is: {user_input}
"""

print(colored(user_input, "magenta"))
# print(prompt)

start_time = time.time()
response = generate_response(prompt)
end_time = time.time()
print(colored(f"GPT answer took {(end_time - start_time):.2f} seconds", "grey"))

md = Markdown(response)
console.print(md)
