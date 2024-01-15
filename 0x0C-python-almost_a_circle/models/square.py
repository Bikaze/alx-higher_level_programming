#!/usr/bin/python3
"""Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Info abou the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size of the square"""
        return self.width

    @size.setter
    def size(self, s):
        """size of the square"""
        self.width = s
        self.height = s

    def update(self, *args, **kwargs):
        """Updates the object attributes"""

        if args:
            self.__updating(*args)
        elif kwargs:
            self.__updating(**kwargs)

    def __updating(self, id=None, size=None, x=None, y=None):
        """implements the updating of attributes"""

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dictionary(self):
        """Returns the dictionary representation of a Square object"""

        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
