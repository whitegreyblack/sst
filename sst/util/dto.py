# dto.py

"""
Basic Data Transfer Object to hold messages and success flag.
"""

from dataclasses import dataclass as struct
from dataclasses import field

@struct
class DTO:
    success: bool = False
    data: list = field(default_factory=lambda: [])
    messages: list = field(default_factory=lambda: [])
    @property
    def message(self):
        return '\n'.join(self.messages)
    def extend(self, other):
        if not isinstance(other, DTO):
            raise TypeError("Cannot extend DTO with a non-DTO object")
        self.success = other.success
        self.messages.extend(other.messages)
    @classmethod
    def todo(cls):
        return cls(messages=["Not yet implemented"])
