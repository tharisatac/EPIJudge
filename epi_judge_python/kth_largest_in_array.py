from typing import List

from test_framework import generic_test

import operator
import random

""" 11.8 """


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:

    def partition_around_pivot(left, right, pivot_idx):
        """
        Partition (NOT SORT) based on the current pivot index. Return the new
        pivot index
        """
        pivot_value = A[pivot_idx]
        new_pivot_idx = left
        # We'll swap this back later!
        A[pivot_idx], A[right] = A[right], A[pivot_idx]

        for i in range(left, right):
            if operator.gt(A[i], pivot_value):
                A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                new_pivot_idx += 1

        # Swap back the pivot_idx with the new pivot_idx
        A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
        return new_pivot_idx

    left = 0
    right = len(A) - 1

    while left <= right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx)

        # It's k-1 because the numbering starts from 1!
        if new_pivot_idx == k - 1:
            return A[new_pivot_idx]
        elif new_pivot_idx < k - 1:
            left = new_pivot_idx
        else:
            right = new_pivot_idx


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "kth_largest_in_array.py", "kth_largest_in_array.tsv", find_kth_largest
        )
    )
