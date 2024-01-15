import unittest
from models.square import Square
"""TestSquare class"""


class TestSquare(unittest.TestCase):
    """Unittests for the 'Square' class"""

    def test_instantiation(self):
        """Checks whether the ids are assigned properly on instantiation"""
        shape = Square(10)
        self.assertIsInstance(shape, Square)
        self.assertEqual(shape.id, 1)
        shape = Square(2, 0, 0, 12)
        self.assertIsInstance(shape, Square)
        self.assertEqual(shape.id, 12)
        shape = Square(1)
        self.assertIsInstance(shape, Square)
        self.assertEqual(shape.id, 2)

    def test_variables(self):
        """Check private attributes and their getter and setter methods"""
        shape = Square(10)
        self.assertEqual(shape.width, 10)
        self.assertEqual(shape.height, 10)
        shape.size = 12
        self.assertEqual(shape.width, 12)
        self.assertEqual(shape.height, 12)

        with self.assertRaises(AttributeError):
            print(shape.__width)
