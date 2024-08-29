from typing import List

from test_framework import generic_test

""" 12.9 """


def longest_contained_range(A: List[int]) -> int:
    """Find the longest contained range"""

    unprocessed_entries = set(A)

    result = 0

    while unprocessed_entries:
        a = unprocessed_entries.pop()

        # Find the lower bound
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        # Find the upper bound
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        if upper_bound - lower_bound - 1 > result:
            # - 1 as it's inclusive
            result = upper_bound - lower_bound - 1

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "longest_contained_interval.py",
            "longest_contained_interval.tsv",
            longest_contained_range,
        )
    )
