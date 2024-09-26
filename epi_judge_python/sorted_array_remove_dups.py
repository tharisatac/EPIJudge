import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

""" 5.5 """


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    """Return the valid entries after deletion, remove any entries in place."""

    # 1) Brute force method would to store each value in a hash table. Each
    # value is then copied back into A.

    # 2) A better method, which uses O(n) operations and O(1) space is to
    # instead of shifting everything left, to overwrite the entries.

    # Handle edge cases
    if not A:
        return 0

    write_idx = 1
    for i in range(1, len(A)):
        if A[write_idx - 1] != A[i]:
            A[write_idx] = A[i]
            write_idx += 1

    return write_idx


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_array_remove_dups.py",
            "sorted_array_remove_dups.tsv",
            delete_duplicates_wrapper,
        )
    )
