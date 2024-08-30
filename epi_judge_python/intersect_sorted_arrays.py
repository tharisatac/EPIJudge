from typing import List

from test_framework import generic_test

""" 13.1 """


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    """Compute the intersection of two arrays"""

    # Use 2 pointers to do this.

    i, j, intersection = 0, 0, []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if A[i] not in intersection:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return intersection


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intersect_sorted_arrays.py",
            "intersect_sorted_arrays.tsv",
            intersect_two_sorted_arrays,
        )
    )
