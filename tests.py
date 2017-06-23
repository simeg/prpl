#!/usr/bin/env python3

import unittest
from tokenizer import *
from parser import *

class TestTokenize(unittest.TestCase):

    def test_simple_numbers(self):
        self.assertEqual(tokenize('3'), [('3')])
        self.assertEqual(tokenize('+3'), [('+3')])
        self.assertEqual(tokenize('-4'), [('-4')])
        self.assertEqual(tokenize('3.5'), ['3.5'])
        self.assertEqual(tokenize('-2-4'), ['-2-4'])

    def test_article_example(self):
        self.assertEqual(tokenize("(begin (define r 10) (* pi (* r r)))"), ['(', 'begin', '(', 'define', 'r', '10', ')', '(', '*', 'pi', '(', '*', 'r', 'r', ')', ')', ')'])


class TestParser(unittest.TestCase):

    def test_parse_article_example(self):
        self.assertEqual(parse("(begin (define r 10) (* pi (* r r)))"), ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]])

    def test_create_ast(self):
        self.assertEqual(create_ast(['(', '+', '2', '3', ')']), ['+', 2, 3])
        self.assertEqual(create_ast(['(', '(', '+', '2', '3', ')', '(', '*', '3', '2', ')', ')']), [['+', 2, 3], ['*', 3, 2]])
        self.assertEqual(create_ast(['(', '(', '+', '2', '3', ')', '(', '*', 'pi', '(', '*', '2', '2', ')', ')', ')']), [['+', 2, 3], ['*', 'pi', ['*', 2, 2]]])


if __name__ == '__main__':
    unittest.main()
