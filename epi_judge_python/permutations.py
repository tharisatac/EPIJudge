from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    """Compute the permutations of A"""

    def _permutate(i):
        if i == len(A) - 1:
            result.append(A.copy())

        for j in range(i, len(A)):
            # First swap A[i] and A[j]
            A[i], A[j] = A[j], A[i]
            # Find all the permutations of A[i+1:]
            _permutate(i + 1)
            # Swap back
            A[i], A[j] = A[j], A[i]

    result: List[List[int]] = []
    _permutate(0)

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "permutations.py",
            "permutations.tsv",
            permutations,
            test_utils.unordered_compare,
        )
    )
