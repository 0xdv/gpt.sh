from termcolor import colored

last_result = "last-result"
knowledge_file = "knowledge.md"

def save_last_result(response: str):
  with open(last_result, "w") as file:
    file.write('\n\n# NOTE:\n')
    file.write(response)

def save_knowledge():
    with open(last_result, "r") as result_file:
        note = result_file.read()
        with open(knowledge_file, "a") as file:
            file.write(note)
    print(colored("The note added to knowledge file", 'green'))
