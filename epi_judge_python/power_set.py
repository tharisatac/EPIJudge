from typing import List

import math
from test_framework import generic_test, test_utils

""" 15.5"""


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    """Generates a power subset: https://www.youtube.com/watch?v=REOH22Xwdkk"""

    # 1) Brute force algorithm using recursion.

    # result = []
    # subset = []

    # def dfs(i):
    #     # We are now out of bounds (i.e. at a leaf node in the tree)
    #     if i >= len(input_set):
    #         # Append a copy of the current subset.
    #         return result.append(subset.copy())

    #     # Go down the branch of adding the number
    #     subset.append(input_set[i])
    #     dfs(i + 1)

    #     # Go down the branch of NOT adding the number
    #     subset.pop()
    #     dfs(i + 1)

    # dfs(0)
    # return result

    # 2) Using bit manipulation

    result = []

    for i in range(1 << len(input_set)):
        bit_array = i

        subset = []
        while bit_array:
            # Isolate the lowest set bit
            subset.append(input_set[int(math.log2(bit_array & ~(bit_array - 1)))])

            # Remove the bit that was just set
            bit_array &= bit_array - 1

        result.append(subset)

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "power_set.py",
            "power_set.tsv",
            generate_power_set,
            test_utils.unordered_compare,
        )
    )
