from typing import Iterator, List
import itertools
import heapq

from test_framework import generic_test

""" 10.3 """


def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    """Sort a k-sorted array"""

    min_heap: List[int] = []

    # Populate the min heap with the first k elements
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    result = []
    # Remember that sequence is an iterator so you're not starting at the
    # beginning but at k+1. So for every new element, push it onto the heap.
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # Sequence is exhausted. Extract the remaining elements from min_heap
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py",
            "sort_almost_sorted_array.tsv",
            sort_approximately_sorted_array_wrapper,
        )
    )
