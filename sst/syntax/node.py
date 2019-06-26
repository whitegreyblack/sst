# node.py

"""Holds parser node values and properties"""

from dataclasses import dataclass as struct
from dataclasses import field
from syntax.token import TokenType


@struct
class Node:
    action: object = None
    data: list = field(default_factory=lambda: [])
    def __repr__(self):
        data = ', '.join(d.text for d in self.data)
        return f"Node(action={self.action.text}, data='{data}')"

