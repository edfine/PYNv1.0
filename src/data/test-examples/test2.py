import unittest

class MyTest(unittest.TestCase):

    def test_fail(self):
        assert False

    def test_fail_message(self):
        assert False, 'This is an assertion message'

    def test_math(self):
        assert 1 + 1 == 2, 'Math is broken'
