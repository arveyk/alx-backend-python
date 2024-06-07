#!/usr/bin/env python3
"""Module to explore duck typing
"""
from collections.abc import Sequence


def element_length(lst: list[int]) -> tuple(int, int):
    """Function that return the length of an iterable
    Args:
        lst: list whose length is to be evaluated
    Returns: the list length
    """
    return [(i, len(i)) for i in lst]
