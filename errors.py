#!/usr/bin/env python3

class SyntaxException(Exception):
    pass


class ElementNotFoundException(Exception):
    pass


class UnexpectedEndOfFileException(Exception):
    pass


class UnknownException(Exception):
    pass

exception_types = {
        'syntax': SyntaxException,
        'element_not_found': ElementNotFoundException,
        'unexpected_end_of_file': UnexpectedEndOfFileException,
        }


def throw_error(err_type, msg=''):
    if err_type in exception_types:
        raise exception_types[err_type](msg)
    else:
        raise UnknownException('Unknown exception type: %s' % err_type)

