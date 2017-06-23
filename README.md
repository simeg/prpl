# prpl
A minimal programming language being written in Python 3. Inspired by [kimi](https://github.com/vakila/kimi).

# TODO for MVP
- Read [1] and [2].
- Taken from kimi:
>Tokenize the program, parse the tokens into a tree, then evaluate the tree. Return the result, or an error message.

[1] http://eloquentjavascript.net/11_language.html
[2] http://norvig.com/lispy.html

- [x] Write tokenizer
- [ ] Test tokenizer
- [x] Write parser
- [ ] Test parser
- [ ] Write evaluator 
- [ ] Test evaluator
- [ ] Write REPL 
- [ ] Test REPL
 
# Interpreter
1. Verify syntactic rules
2. Parse into AST (abstract syntax tree)
3. Pass AST on to evaluation/execution

# Tools to use
- [CI](https://circleci.com/)

