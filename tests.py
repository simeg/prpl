import unittest
from tokenizer import *

class TestTokenize(unittest.TestCase):

    def test_numbers(self):
        # Valid number literals
        self.assertEqual(tokenize("3"), [('literal', 3)])
        self.assertEqual(tokenize("+3"), [('literal', 3)])
        self.assertEqual(tokenize("-4"), [('literal', -4)])
        # Not valid (considered symbols)
        self.assertEqual(tokenize("3.5"), [('symbol', '2.5')])
        self.assertEqual(tokenize("-2-4"), [('symbol', '-2-4')])

