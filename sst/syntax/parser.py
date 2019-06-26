# interpret.py

"""Parses tokenized statements into nodes"""

from syntax.tokenizer import tokenize
from syntax.token import TokenType
from syntax.node import Node


def parse(tokens: list) -> object:
    """
    Reads tokens to create a simple abstract syntax tree
    """
    nodes = []
    if not tokens:
        return nodes 
    while tokens:
        # iterate action nodes
        token, *tokens = tokens
        if token.type is not TokenType.NAME:
            raise Exception(f"{token} is not an NAME token")
        node = Node(action=token)
        while tokens:
            token, *tokens = tokens
            if token.type is TokenType.END:
                break
            
            node.data.append(token)
        nodes.append(node)
    return nodes

def handle_input(user_input):
    """
    function hook to pass into repl loop
    """
    output = []
    tokens = tokenize(user_input)
    interpreted = parse(tokens)
    if interpreted:
        output.append(str(interpreted))
    return output

if __name__ == "__main__":
    from util.repl import user_input
    from util.reader import from_file
    from util.output_handler import handle_output
 
    from_file(handle_input, handle_output, 'instructions.txt')
    user_input(handle_input, handle_output)

