from typing import List

from test_framework import generic_test, test_utils

""" 15.5"""


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    """Generates a power subset: https://www.youtube.com/watch?v=REOH22Xwdkk"""

    result = []
    subset = []

    def dfs(i):
        # We are now out of bounds (i.e. at a leaf node in the tree)
        if i >= len(input_set):
            # Append a copy of the current subset.
            return result.append(subset.copy())

        # Go down the branch of adding the number
        subset.append(input_set[i])
        dfs(i + 1)

        # Go down the branch of NOT adding the number
        subset.pop()
        dfs(i + 1)

    dfs(0)
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
