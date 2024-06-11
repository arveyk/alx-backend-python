#!/usr/bin/env python3
""" Module for creating async generator functions
"""


async def async_generator():
    """ Generator function
    Args : none
    Returns: yields some numbers
    """
    import asyncio
    import random

    for i in range(10):
        rand_number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand_number
