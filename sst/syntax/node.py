# node.py

"""
Holds node values and properties
"""

from dataclasses import dataclass as struct
from dataclasses import field

@struct
class Node:
    data: int = 0
    count: int = 1
    parent: object = None
    left: object = None
    right: object = None
    def __repr__(self):
        return str(self)
    def __str__(self):
        l = self.left.data if self.left else None
        r = self.right.data if self.right else None
        return f"Node(data={self.data}, left={l}, right={r})"
    @property
    def leaf(self):
        return not (self.left or self.right)
