import heapq
from typing import Iterator, List

from test_framework import generic_test

""" 10.5 """


def online_median(sequence: Iterator[int]) -> List[float]:
    """Find the rolling median of a sequence."""

    # Use a Max Heap to store the smaller half and a Min Heap to store the
    # larger half. Keep both heaps the same size, otherwise keep the min-heap
    # at most one size larger than the max heap.

    min_heap: list[int] = []
    max_heap: list[int] = []

    result: list[int] = []

    for s in sequence:
        # Everything that is stored must be negative in a max heap
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, s))

        # Ensure they have an equal number of elements. Otherwise, min_heap must
        # have one more.
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        result.append(
            0.5 * (min_heap[0] + -max_heap[0])
            if len(max_heap) == len(min_heap)
            else min_heap[0]
        )

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "online_median.py", "online_median.tsv", online_median_wrapper
        )
    )
