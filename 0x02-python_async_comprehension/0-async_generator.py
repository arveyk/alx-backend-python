#!/usr/bin/env python3
""" Module for creating async generator functions
"""
import asyncio
import random


async def async_generator() -> float:
    """
    Generator function that loops 10 times and yields a number each time
    Args:
        None
    Returns: yields some numbers
    """
    for i in range(10):
        rand_number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand_number
