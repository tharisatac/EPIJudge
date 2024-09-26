from typing import List

from test_framework import generic_test

""" 17.4 """


def _has_two_sum(A: list[int], t: int) -> bool:
    """Return True if there exists a sum of numbers which add up to t."""

    # O(n)
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] > t:
            j -= 1
        else:
            i += 1

    return False


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()

    # OO(n)
    return any(_has_two_sum(A, t - a) for a in A)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("three_sum.py", "three_sum.tsv", has_three_sum))
