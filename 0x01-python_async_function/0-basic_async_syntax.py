#!/usr/bin/env python3
"""Writing asyncronous routines that generates a random number
and wints for the amount of time equal to that generated number
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Function that waits for some second
    Args:
        max_delay: the maximum amount of time to wait
    Returns: amount of time it delayed
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
