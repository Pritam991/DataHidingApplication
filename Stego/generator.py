
import math
from typing import Iterator





def identity() -> Iterator[int]:
    """f(x) = x"""
    n = 0
    while True:
        yield n
        n += 1