#!/usr/bin/env python3
"""Module for function that measures runtime
"""
import time
import asyncio
from typing import Never

asyncCom = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> Never:
    """
    Function to measure runtime
    Args:
        None
    Returns: the total amout of time it takes to execute an async function
    """
    start = time.perf_counter()
    await asyncio.gather(asyncCom(), asyncCom(), asyncCom(), asyncCom())
    elapsed_t = time.perf_counter() - start
    return elapsed_t
