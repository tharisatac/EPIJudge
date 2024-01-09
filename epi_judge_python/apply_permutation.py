from typing import List

from test_framework import generic_test

""" 5.10 """


def apply_permutation(perm: List[int], A: List[int]) -> None:
    """Apply permutation to the passed in array, A."""

    assert len(perm) == len(A)

    # 1) A simple solution would be to allocate additional storage.
    # B = [0] * len(A)

    # for i in range(len(A)):
    # B[perm[i]] = A[i]

    # for j in range(len(B)):
    # A[j] = B[j]

    # 2) With no additional storage, this may be more complicated.
    for i in range(len(A)):
        # We move it until that element in perm matches the index.
        while perm[i] != i:
            # Swap the elements in A
            A[perm[i]], A[i] = A[i], A[perm[i]]
            # Swap the corresponding indices in perm as A has now been moved.
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "apply_permutation.py", "apply_permutation.tsv", apply_permutation_wrapper
        )
    )
