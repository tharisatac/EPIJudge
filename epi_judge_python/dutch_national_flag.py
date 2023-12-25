import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    """Utilize QuickSort to solve the Dutch Flag Partition problem."""
    pivot = A[pivot_index]

    # 1) A naive approach would be to utilize 3 arrays.
    # 2) A better approach, is to do the change in place using pointers.
    # Initialize pointers.
    low = 0
    high = len(A) - 1
    curr = 0

    while curr <= high:
        if A[curr] < pivot:
            A[low], A[curr] = A[curr], A[low]
            curr += 1
            low += 1
        elif A[curr] > pivot:
            A[high], A[curr] = A[curr], A[high]
            high -= 1
        else:
            curr += 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure("Not partitioned after {}th element".format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "dutch_national_flag.py",
            "dutch_national_flag.tsv",
            dutch_flag_partition_wrapper,
        )
    )
