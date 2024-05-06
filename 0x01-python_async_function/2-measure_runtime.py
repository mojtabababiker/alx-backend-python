#!/usr/bin/env python3
"""
Interducing async approach in pytyon
"""
import asyncio
from typing import List, Callable
from time import perf_counter

wait_n: Callable[[int, int], List[float]] = __import__(
    '1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the execution time of wait_n(n, max_delay)
    and returns it
    """
    start: float = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (perf_counter() - start) / n
