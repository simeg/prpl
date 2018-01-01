#!/usr/bin/env python3

from .errors import throw_error

from src.tokenizer import tokenize

# TODO: Remove these, I don't want to implement Scheme.
# I want to create my own language
Symbol = str
List = list
Number = (int, float)


def parse(program):
    "Read a Scheme expression from a string."
    return create_ast(tokenize(program))


def create_ast(tokens):
    "Create an Abstract Syntax Tree from provided tokens."
    if len(tokens) == 0:
        throw_error('unexpected_end_of_file', 'Unexpected EOF while reading')
    token = tokens.pop(0)
    if token == '(':
        expr = []
        while tokens[0] != ')':
            expr.append(create_ast(tokens))
        tokens.pop(0)  # pop off ')'
        return expr
    elif token == ')':
        throw_error('unexpected_symbol', 'Unexpected )')
    else:
        return atom(token)


def atom(token):
    "Numbers become numbers, every other token is a symbol."
    try:
        return int(token)
    except ValueError:
        # int() throws ValueError if token has any decimals
        try:
            return float(token)
        except ValueError:
            # If parsing to int and float fails, return as Symbol
            return Symbol(token)
