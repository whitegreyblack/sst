# tokenizer.py

"""
parses text or file input into token types.

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

from syntax.token import TokenType, Token, op_token_types as Ops

space = ' ' 
numeric = set('1234567890')
alphabet = set('abcdefghijklmnopqrstuvwxyz')
symbols = set('!@#$%^&*()-_+=/[]{},.<>;:\'"\\|')

def is_valid(x):
    return x is not None

def is_number(x):
    return x in numeric

def is_letter(x):
    return x in alphabet

def is_symbol(x):
    return x in symbols

def next_char(text, pos) -> [str, None]:
    return text[pos] if (pos <= len(text) - 1) else None

def mixed_error(text, pos):
    return f"""
  Syntax error. Found mixed characters in word:
    {text}
    {' ' * pos}^"""[1:]

def invalid_error(text, pos):
    return f"""
  Syntax error. Found invalid characters on token:
    {text}
    {' ' * pos}^"""[1:]

def tokenize(text) -> list:
    """
    Parses input and returns valid input as typed tokens

    If token starts with a:
        * character -> word (this will be messed up if b' or r' is introduced
        * number -> int || float
    
    Currently does not handle special characters
    """
    stack = []
    tokens = []
    if not text:
        return tokens
    beg, pos = 0, 0
    char = next_char(text, pos) 
    while char is not None:
        # consume chars until EOL
        char_is_valid = True
        if char is space:
            # consume characters until next non space char
            char_is_space = True
            while char_is_valid and char_is_space:
                pos += 1
                char = next_char(text, pos)
                char_is_valid = is_valid(char)
                char_is_space = char is space
            continue
        beg = pos
        if is_letter(char):
            # consume characters until not letter char
            char_is_alpha = True
            while char_is_valid and char_is_alpha:
                pos += 1
                char = next_char(text, pos)
                char_is_valid = is_valid(char)
                char_is_alpha = is_letter(char)
            if is_number(char) or is_symbol(char):
                print(mixed_error(text, pos))
                return tokens
            if not char_is_valid or char is space:
                tokens.append(Token(text[beg:pos], TokenType.NAME))
        elif is_number(char):
            tokens += stack
            stack = []
            char_is_number = True
            while char_is_valid and char_is_number:
                pos += 1
                char = next_char(text, pos)
                char_is_valid = is_valid(char)
                char_is_number = is_number(char)
            if is_letter(char):
                print(mixed_error(text, pos))
                return tokens
            if is_symbol(char) or not char_is_valid or char is space:
                stack.append(Token(text[beg:pos], TokenType.NUMBER))
                # tokens.append(Token(text[beg:pos], TokenType.NUMBER))
        elif is_symbol(char):
            # This is the only block to use the ExactTokenTypes class
            char_is_symbol = True
            while char_is_valid and char_is_symbol:
                pos += 1
                char = next_char(text, pos)
                char_is_valid = is_valid(char)
                char_is_symbol = is_symbol(char)
            if is_letter(char):
                print(mixed_error(text, pos))
                return tokens
            if is_number(char) or not char_is_valid or char is space:
                symbol = text[beg:pos]
                tokentype = Ops.get(symbol, TokenType.OP)
                tokens.append(Token(symbol, tokentype))
                tokens += stack
                stack = []
        else:
            print(invalid_error(text, pos))
            return tokens
    tokens += stack
    tokens.append(Token('', TokenType.END))
    return tokens

def handle_input(input_stream):
    """
    function hook to pass into repl loop
    """
    output = []
    tokens = tokenize(input_stream)
    for token in tokens:
        output.append(f"{token.type} {token.text}")
    return output

if __name__ == "__main__":
    from util.repl import user_input
    from util.reader import from_file
    from util.output_handler import handle_output

    from_file(input_handler=handle_input, 
              output_handler=handle_output, 
              file_name='instructions.txt')
    user_input(input_handler=handle_input, output_handler=handle_output)

