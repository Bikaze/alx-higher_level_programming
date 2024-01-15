import unittest
from models.base import Base
"""TestBase class"""


class TestBase(unittest.TestCase):
    """Unittests for the 'Base' class"""

    def test_instantiation(self):
        """Checks whether the ids are assigned properly on instantiation"""
        shape = Base()
        self.assertIsInstance(shape, Base)
        self.assertEqual(shape.id, 1)
        shape = Base(5)
        self.assertIsInstance(shape, Base)
        self.assertEqual(shape.id, 5)
        shape = Base()
        self.assertIsInstance(shape, Base)
        self.assertEqual(shape.id, 2)
