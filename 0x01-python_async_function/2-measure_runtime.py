#!/usr/bin/env python3
"""
Module for 1-concurrent_coroutine
for executing multiple coroutines
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Function that masures the time it takes to execute a function
    Args:
        n: some number
        max_delay: the maximum amount of time to wait
    Returns: amount of time used
    """
    start_time = time.perf_counter()
    task = wait_n(n, max_delay)
    await task
    time_elapse = time.perf_counter() - start_time
    return time_elapse
