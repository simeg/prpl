import unittest
from tokenizer import *

class TestTokenize(unittest.TestCase):

    def test_numbers(self):
        # Valid number literals
        self.assertEqual(tokenize('3'), [('3')])
        self.assertEqual(tokenize('+3'), [('+3')])
        self.assertEqual(tokenize('-4'), [('-4')])
        # Not valid (considered symbols)
        self.assertEqual(tokenize('3.5'), ['3.5'])
        self.assertEqual(tokenize('-2-4'), ['-2-4'])

if __name__ == '__main__':
    unittest.main()
