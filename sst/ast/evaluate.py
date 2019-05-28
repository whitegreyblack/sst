# evaluate.py

"""
Evaluates typed tokens from interpret.py
"""

from dataclasses import dataclass as struct
from ast.interpret import LETTER, NUMBER, tokenize
from tree.dto import DTO
import difflib

@struct
class Statement:
    func: str
    args: list

actions = {
    'insert',
    'find'
}

def evaluate(tokens):
    dto = DTO()
    while tokens:
        token = tokens.pop(0)
        if token.type == LETTER:
            if token.text in actions:
                dto.messages.append(f"action: {token.text}")
            else:
                commands_accepted = "\t" + "\n".join(actions)
                dto.messages.append(f"""
eval: '{token.text}' is not a valid command. 
Commands accepted: {commands_accepted}"""[1:])
                close_match = difflib.get_close_matches(token.text, actions)
                if close_match:
                    dto.messages.append(f"""
\nThe most similar command is:\n\t{close_match.pop()}"""[1:])
                break
        else:
            dto.messages.append(f"arg: {token.text}")
    dto.success = True
    return dto

def handle_input(user_input):
    output = []
    tokens = tokenize(user_input)
    response = evaluate(tokens)
    output.append(response.message)
    return output

if __name__ == "__main__":
    from ast.repl import user_input
    import sys

    if sys.argv[1:]:
        if sys.argv[1] == '--help':
            print("python -m evaluate")

    user_input(input_handler=handle_input)
