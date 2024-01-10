#!/usr/bin/python3
"""
class Rectangle(BaseGeometry)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle. It inherits from BaseGeometry"""

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self._width = width
        self._height = height
