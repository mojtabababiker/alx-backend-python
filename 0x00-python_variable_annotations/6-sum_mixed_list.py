#!/usr/bin/env python3
"""
Python Vaiable Annotaions presentation on code
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Annotaed function that sum a list of float | int and
    return the value as float
    """
    sum: float = 0.0
    for num in mxd_list:
        sum += num

    return sum
