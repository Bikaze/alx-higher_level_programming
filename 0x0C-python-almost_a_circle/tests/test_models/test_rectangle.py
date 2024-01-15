import unittest
from models.rectangle import Rectangle
"""TestRectangle class"""


class TestRectangle(unittest.TestCase):
    """Unittests for the 'Rectangle' class"""

    def test_instantiation(self):
        """Checks whether the ids are assigned properly on instantiation"""
        shape = Rectangle(10, 2)
        self.assertIsInstance(shape, Rectangle)
        self.assertEqual(shape.id, 1)
        shape = Rectangle(5, 2, 0, 0, 12)
        self.assertIsInstance(shape, Rectangle)
        self.assertEqual(shape.id, 12)
        shape = Rectangle(1, 2)
        self.assertIsInstance(shape, Rectangle)
        self.assertEqual(shape.id, 2)

    def test_variables(self):
        """Check private attributes and their getter and setter methods"""
        shape = Rectangle(10, 2)
        self.assertEqual(shape.width, 10)
        self.assertEqual(shape.height, 2)
        shape.width = 12
        shape.height = 4
        self.assertEqual(shape.width, 12)
        self.assertEqual(shape.height, 4)

        with self.assertRaises(AttributeError):
            print(shape.__width)
