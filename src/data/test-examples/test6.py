import unittest
from .simple_math import add, subtract, multiply, divide

class MyTest(unittest.TestCase):

    def setUp(self):
        self.x = 1
        self.y = 1
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_add(self):
        self.assertEqual(add(self.x, self.y), 2)

    def test_subtract(self):
        self.assertEqual(subtract(self.x, self.y), 0)

    def test_multiply(self):
        self.assertEqual(multiply(self.x, self.y), 1)

    def test_divide(self):
        self.assertEqual(divide(self.x, self.y), 1)
