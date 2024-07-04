#!/usr/bin/env python3
"""Module - 7-to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """The function returns a tuple containing the first
    element as a string and the second element as a float
    """
    return (k, float(v**2))
