#!/usr/bin/env python3
"""
Interducing async approach in pytyon
"""
import asyncio
from typing import List, Callable


wait_random: Callable[[int], float] = __import__(
    '0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An async routine that called wait_random n times with
    the max_delay, and returns the returned values of it
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(
        *tasks
    )
    return sorted(results)
