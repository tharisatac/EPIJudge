from typing import List

from test_framework import generic_test

""" 11.3 """


def search_smallest(A: List[int]) -> int:
    """Search a cyclically sorted array."""

    left, right = 0, len(A) - 1

    while left < right:
        mid = (left + right) // 2

        if A[mid] > A[right]:
            # If the middle is greater than the right, then the smallest number
            # must be betwee A[mid+1] and A[right]
            left = mid + 1
        else:
            # If A[mid] <= A[right], then the smallest number must be between
            # A[left] and A[mid]
            right = mid

    return left


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_shifted_sorted_array.py",
            "search_shifted_sorted_array.tsv",
            search_smallest,
        )
    )
