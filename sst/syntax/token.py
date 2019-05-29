# ast_token.py

"""
Holds different grammar and syntax token classes
"""

# regexes from library to recognize numbers
from tokenize import Floatnumber, Intnumber, Name, group, _compile 
from dataclasses import dataclass as struct
from dataclasses import field

class TokenType:
    OP = 'OP'
    NAME = 'NAME'
    NUMBER = 'NUMBER'

op_token_types = {
    '.': 'DOT',
    '..': 'RANGE_INCL',
    '...': 'RANGE_EXCL',
    '-': 'DOT',
    '+': 'PLUS',
    '->': 'RARROW'
}

@struct
class Token:
    text: str
    type: str

if __name__ == "__main__":
    print(Token('->', op_token_types.get('->', TokenType.OP)))

