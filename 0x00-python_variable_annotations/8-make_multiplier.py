#!/usr/bin/env python3
"""
Python Vaiable Annotaions presentation on code
"""
from typing import Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Annotaed function that take float and return
    a function that multiply value by that float
    """
    def f(x: float) -> float:
        """
        multiply x with outer multiplier number
        and return the value
        """
        return x * multiplier

    return f
