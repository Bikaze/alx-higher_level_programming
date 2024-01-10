#!/usr/bin/python3
"""
class Square(Rectangle)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a Square. It inherits from Rectangle Class"""

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator('size', size)
        self._size = size
