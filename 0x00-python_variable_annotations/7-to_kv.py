#!/usr/bin/env python3
"""Module to define function for returning a tuple made up of
the arguments it is supplied
"""


def to_kv(k: str, v: int | float) -> tuple:
    """Function that returns a tuple consisting of the arguments it is
    supplied
    Args:
       k: the 'key' of the tuple
       v: the number to be supplied
    Returns: a tupple"""

    tup = (k, v)
    return tup
