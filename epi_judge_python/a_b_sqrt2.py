from typing import List

import math
import bintrees

from test_framework import generic_test

""" 14.7 """


class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = a + b * math.sqrt

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    """Generate the smallest k a + b_sqrt(2)"""

    # Use a binary tree to do this! It is way easier because we can always get
    # the smallest value.

    # Initial is 0 + 0 sqrt(2)
    candidates = bintrees.RBTree([(Number(0, 0), None)])

    result: List[float] = []
    while len(result) < k:
        next_smallest = candidates.pop_min()[0]
        result.append(next_smallest.val)

        candidates[Number((next_smallest.a + 1, next_smallest.b))] = None
        candidates[Number((next_smallest.a, next_smallest.b + 1))] = None

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "a_b_sqrt2.py", "a_b_sqrt2.tsv", generate_first_k_a_b_sqrt2
        )
    )
