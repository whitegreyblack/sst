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

from tree import Tree
print(Tree.actions)

def evaluate(tokens):
    dto = DTO()
    while tokens:
        token = tokens.pop(0)
        if token.type == LETTER:
            if token.text in Tree.actions:
                dto.messages.append(f"action: {token.text}")
            else:
                dto.messages.append(f"eval: '{token.text}' is not a valid command. See 'eval --help'.")
                close_match = difflib.get_close_matches(token.text, Tree.actions)
                if close_match:
                    dto.messages.append(f"\nThe most similar command is:\n\t{close_match.pop()}")
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
    user_input(fn=handle_input)
