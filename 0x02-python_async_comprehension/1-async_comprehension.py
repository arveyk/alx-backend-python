#!/usr/bin/env python3
""" Module for creating async generator functions
"""
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Function to implement async comprehension
    Args:
        None
    Returns: list of the amount of waiting time
    """
    result = [rand_num async for rand_num in async_generator()]
    return result
