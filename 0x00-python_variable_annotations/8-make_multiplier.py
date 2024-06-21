#!/usr/bin/env python3
"""Module to define a function that returns a function multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that takes an argument and return a function that
    multiplies that number by a fixed multiplier
    Args:
        multiplier: a number to multiply by
    Return: the function to do the multiplication
    """

    def mul(num: float) -> float:
        """Function that mutiplies
        Args:
            num: number to multiply
        Returns: result
        """
        return multiplier * num

    return mul
