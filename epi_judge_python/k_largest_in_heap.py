import heapq
from typing import List

from test_framework import generic_test, test_utils

""" 10.6 """


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    """Without modifying A, find the K-largest values."""

    if k <= 0:
        return []

    # Store the (-value, index) pair in the max-heap. Use negative values to
    # emulate the max heap.
    candidate_max_heap = []

    # The largest element in A is at index 0.
    candidate_max_heap.append((-A[0], 0))

    # Store the results
    result = []

    for _ in range(k):
        c_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])

        left_c_idx = 2 * c_idx + 1
        if left_c_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[left_c_idx], left_c_idx))

        right_c_idx = 2 * c_idx + 2
        if right_c_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[right_c_idx], right_c_idx))

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare,
        )
    )
