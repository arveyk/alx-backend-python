#!/usr/bin/env python3
"""Module to define an annotated function
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """Function to add a list of floats
    Args:
        input_list: a list of numbers to be summed
    Return: sum of the numbers"""
    summation = 0
    for number in input_list:
        summation += number
    return summation
