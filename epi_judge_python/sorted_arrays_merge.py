from typing import List

from test_framework import generic_test
import heapq

""" 10.1 """


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    """Merge sorted arrays using a min-heap"""

    # First set up the min-heap
    min_heap: List[tuple[int, int]] = []
    # Set up a sorted array of iters
    sorted_arrays_iter = [iter(x) for x in sorted_arrays]

    # Put first element from each iter into the min-heap
    for i, it in enumerate(sorted_arrays_iter):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_entry_idx = heapq.heappop(min_heap)
        result.append(smallest_entry)

        smallest_entry_iter = sorted_arrays_iter[smallest_entry_idx]
        next_element = next(smallest_entry_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_entry_idx))

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays
        )
    )
