#!/usr/bin/env python3

from tokenizer import tokenize

# TODO: Extract to separate file
Symbol = str


def parse(program):
    "Read a Scheme expression from a string."
    return create_ast(tokenize(program))


def create_ast(tokens):
    "Create an Abstract Syntax Tree from provided tokens."
    if len(tokens) == 0:
        raise SyntaxError('Unexpected EOF while reading')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(create_ast(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('Unexpected )')
    else:
        return atom(token)


def atom(token):
    "Numbers become numbers; every other token is a symbol."
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)
