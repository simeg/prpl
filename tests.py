#!/usr/bin/env python3

import unittest
from tokenizer import *
from my_parser import parse, create_ast
from errors import *
from evaluator import *


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


class TestErrors(unittest.TestCase):

    def test_throw_error(self):
        self.assertRaises(SyntaxException, lambda: throw_error('syntax', 'irrelevant-err-msg'))

    def test_throw_unknown_error(self):
        self.assertRaises(UnknownException, lambda: throw_error('non-existing-type', 'irrelevant-err-msg'))

class TestEval(unittest.TestCase):

    def test_procedure_call(self):
        self.assertEqual(eval(['=', 2, 0]), False)
        # Test that variable reference replacement works
        # The add fn has to be mocked because the entire environment is passed
        self.assertEqual(eval(['+', 'foo', 5], {'+': lambda x,y:x+y, 'foo': 5}), 10)
        # Test that conditionals work
        self.assertEqual(eval(['if', ['=', True, True], 10, 20]), 10)


if __name__ == '__main__':
    unittest.main()
