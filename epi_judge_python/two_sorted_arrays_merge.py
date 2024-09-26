from typing import List

from test_framework import generic_test

""" 13.2 """


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    """Merge two sorted arrays in place."""

    # Start from the end.
    a, b, write_idx = m - 1, n - 1, m + n - 1

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1

        write_idx -= 1

    # At this point, all of A would have been moved.
    while b >= 0:
        A[write_idx] = B[b]
        write_idx -= 1
        b -= 1

    return A


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "two_sorted_arrays_merge.py",
            "two_sorted_arrays_merge.tsv",
            merge_two_sorted_arrays_wrapper,
        )
    )
