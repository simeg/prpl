#!/usr/bin/env python3

from environment import *
from errors import throw_error

# TODO: Remove these, I don't want to implement Scheme.
# I want to create my own language
Symbol = str          # A Scheme Symbol is implemented as a Python str
List   = list         # A Scheme List is implemented as a Python list
Number = (int, float) # A Scheme Number is implemented as a Python int or float

def eval(x, env=global_env):
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):      # variable reference
        if x in env:
            return env[x]
        else:
            throw_error('element_not_found', x)
    elif not isinstance(x, List):  # constant literal (a number)
        return x

    elif x[0] == 'if':             # conditional
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt) # evaluate the conditional
        return eval(exp, env)

    elif x[0] == 'define':         # definition
        (_, var, exp) = x
        env[var] = eval(exp, env)

    else:                          # procedure call
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)
