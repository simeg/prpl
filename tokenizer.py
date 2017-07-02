#!/usr/bin/env python3

def tokenize(chars):
    '''Take a program as a string, return the
    tokenized program as a list of strings.

    >>> tokenize("-1")
    [(-1)]

    >>> tokenize("(+ 1 2)")
    ['+', 1, 2)]
    '''
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()
