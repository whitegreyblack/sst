# token.py

"""
Holds different grammar and syntax token classes
"""

from dataclasses import dataclass as struct
from dataclasses import field

@struct
class ActionToken:
    text: str
    type: str

class PrefixTree:
    pass

@struct
class Statement:
    func: str
    args: list
