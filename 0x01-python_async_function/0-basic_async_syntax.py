#!/usr/bin/env python3
"""Writing asyncronous routines
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> int:
    """ Function that waits for some second
    Args:
        max_delay: the maximum amount of time to wait
    Returns: amount of time it delayed
    """
    
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
