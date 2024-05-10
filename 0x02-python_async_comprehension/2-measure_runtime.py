#!/usr/bin/env python3
"""
Messure the runtime of the async_comprehension function
"""
import asyncio
from time import perf_counter
from typing import Callable, List


async_comprehension: Callable[[], List[float]] = __import__(
    '1-async_comprehension'
    ).async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of the async_comprehension function, after
    executing it 4 times in parallel.
    """
    start: float = perf_counter()
    await asyncio.gather( *[async_comprehension() for _ in range(4)])
    return perf_counter() - start
