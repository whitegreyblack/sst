# evaluate.py

"""
Evaluates typed tokens from interpret.py
"""

from syntax.tokenizer import tokenize
from syntax.token import TokenType
from syntax.parser import parse
from util.dto import DTO
import difflib

op_expression = {
    '..': lambda x, y: ' '.join(str(i) for i in range(x, y)),
    '...': lambda x, y: ' '.join(str(i) for i in range(x, y+1))
}

def evaluate(nodes):
    expressions = []
    if not nodes:
        return expressions
    for node in nodes:
        expression = []
        expression.append(node.action.text)
        for arg in node.data:
            if arg.type == TokenType.NUMBER:
                expression.append(arg.text)
        expressions.append(expression)
    return expressions

def handle_input(user_input):
    tokens = tokenize(user_input)
    nodes = parse(tokens)
    expressions = evaluate(nodes)
    return expressions

if __name__ == "__main__":
    from util.repl import user_input
    from util.reader import from_file
    from util.output_handler import handle_output
    """
    import sys

    if sys.argv[1:]:
        if sys.argv[1] == '--help':
            print("python -m evaluate")
    """
    from_file(handle_input, handle_output, 'instructions.txt')
    user_input(input_handler=handle_input, output_handler=handle_output)

