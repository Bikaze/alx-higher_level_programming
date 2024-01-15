#!/usr/bin/python3
"""Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter of the width"""
        self.validate_attribute('width', width)
        self.__width = width

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter of the height"""
        self.validate_attribute('height', height)
        self.__height = height

    @property
    def x(self):
        """the x-coordinate"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter of x"""
        self.validate_attribute('x', x)
        self.__x = x

    @property
    def y(self):
        """the y-coordinate"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter of y"""
        self.validate_attribute('y', y)
        self.__y = y

    def validate_attribute(self, attr, value):
        """takes the attr(attribute name) and its value and validates it"""
        if type(value) != int:
            raise TypeError(f"{attr} must be an integer")
        elif value <= 0 and (attr == 'width' or attr == 'height'):
            raise ValueError(f"{attr} must be > 0")
        elif (attr == 'x' or attr == 'y') and value < 0:
            raise ValueError(f"{attr} must be >= 0")

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.width * self.height

    def __str__(self):
        """print Object representation"""

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -\
 {self.width}/{self.height}"

    def display(self):
        """prints the rectangle instance with the character '#' character"""

        self.y_coor()
        for i in range(self.height):
            self.x_coor()
            for j in range(self.width):
                print('#', end='')
            print()

    def x_coor(self):
        """Simulates the x coordinate"""
        for i in range(self.x):
            print(' ', end='')

    def y_coor(self):
        """Simulates the y coordinate"""
        for i in range(self.y):
            print()
