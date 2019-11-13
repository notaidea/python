# -*- coding: utf-8 -*-

from enum import Enum

class Color(Enum):
     red = "red color"
     blue = "blue color"

print(Color.red.name)
print(Color.red.value)
