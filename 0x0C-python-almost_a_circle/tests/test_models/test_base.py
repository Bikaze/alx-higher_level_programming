import unittest
from models.base import Base
"""TestBase class"""


class TestBase(unittest.TestCase):
    """Unittests for the 'Base' class"""

    def test_instantiation(self):
        shape = Base()
        self.assertIsInstance(shape, Base)
        self.assertEqual(shape.id, 1)
        shape = Base(5)
        self.assertIsInstance(shape, Base)
        self.assertEqual(shape.id, 2)
        shape = Base()
        self.assertIsInstance(shape, Base)
        self.assertEqual(shape.id, 2)
