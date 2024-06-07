#!/usr/bin/env python3
"""Module to define function for summing a list of mixed number types
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """Function that sums a list of integers and/or floats
    Args:
        mxd_lst: list containing numbers to be summed
    Returns: the sum of the numbers"""
    total = 0.00
    for item in mxd_lst:
        total += float(item)
    return total
