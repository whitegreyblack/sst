# ui.py

"""
Visual property classes used in tree classes
"""

from dataclasses import dataclass as struct
from dataclasses import field


class Branch(object):
    Corner = "└──"
    Edge = "├──"
    Line = "│  "
    Blank = "   "
    Empty = ""
