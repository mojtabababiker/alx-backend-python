#!/usr/bin/env python3
"""
Python Vaiable Annotaions presentation on code
"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable) -> List[Tuple[Sequence, int]]:
    """
    Get the length of all the items in the lst, and
    return a list of tuples that contain the item
    and its length
    """
    return [(i, len(i)) for i in lst]
