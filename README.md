# prpl
A minimal programming language (about to be) written in Python 3. Inspired by [kimi](https://github.com/vakila/kimi).

# TODO
- Read [1] and [2] and try to come up with the first step of writing this (what seems like) very complex thing.
- Outline the big steps needing to be done. Taken from kimi:
>Tokenize the program, parse the tokens into a tree, then evaluate the tree. Return the result, or an error message.

[1] http://eloquentjavascript.net/11_language.html
[2] http://norvig.com/lispy.html

# Definitions/Language information
- Variable reference (works as normal variables do)
- Variable definition (`define var exp`)
- Number datatype. Evaluates to itself.
- Conditional `if` (`if test consequence alternative`)
- If proc is anything other than one of the symbols if, define, or quote then it is treated as a procedure. Evaluate proc and all the args, and then the procedure is applied to the list of arg values. Example: (sqrt (* 2 8)) -> 4.0 
- Atomic expressions, things that cannot be broken down into smaller pieces. Examples would be datatypes such as numbers and symbols

# Interpreter
0. Verify syntactic rules
0. Parse into AST (abstract syntax tree)
0. Pass AST on to evaluation/execution

