# interpret.py

"""
@parameter = text: str NOT NONE

parses text or file input into typed tokens.

Analysis:
    This function allows more control and versatility over input than splitting
    user input by spaces. There could be an indeterminate number of whitespace
    or even invalid characters which can be included with user input which
    can be excluded using this function.
    If an input is valid and no errors are found with any tokens, then the 
    function returns with a list of typed tokens containing split text.
    If any errors are found then the error is logged and function returns early
    with an empty token list.
"""

from ast_tokenizer import tokenize

def interpret(tokens) -> object:
    """
    Reads tokens to create a simple abstract syntax tree
    """
    if not tokens:
        return ""
    while tokens:
        token, *tokens = tokens
        if token.type is LETTER:
            # function call
            ts = tokens
            while tokens:
                t, *tokens = tokens
                if t.type is LETTER:
                    ...
                break
        break
    return NotImplemented

def handle_input(user_input):
    """
    function hook to pass into repl loop
    """
    output = []
    tokens = tokenize(user_input)
    for token in tokens:
        output.append(f"{token.text} {token.type}")
    interpreted = interpret(tokens)
    if interpreted:
        output.append(str(interpreted))
    return output

if __name__ == "__main__":
    from repl import user_input
    user_input(fn=handle_input)

