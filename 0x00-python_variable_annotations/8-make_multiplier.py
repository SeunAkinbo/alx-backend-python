#!/usr/bin/env python3
"""Module - 8-make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """The make_multiplier function returns a function
    """
    return lambda x: x * multiplier
