from typing import List

from test_framework import generic_test

""" 5.4 """


def can_reach_end(A: List[int]) -> bool:
    """
    Whether the end of the passed-in array can be reached.

    This can be done using 'offsets'. i.e. the concept that for the i-ith
    entry, the furthest it can reach is i + A[i].

    NOTE: For a certain i, if the furthest that can be reached is i-1 then
    the end cannot be reached.
    """

    furthest_reached = 0
    last_idx = len(A) - 1

    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1

    return furthest_reached >= last_idx


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end
        )
    )
