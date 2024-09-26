from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    """
    Takes in A which is an array of integers and increment it.

    i.e. [1,2,9] -> [1,3,0]
    """
    # 1) Brute force approach is to convert to an integer first (via a string),
    # increment it and change it back into an array.
    # This will be O(n) in time complexity and O(k) in space complexity as a new
    # array of equivalent size is reassigned.

    # num = int("".join(str(a) for a in A))
    # num += 1
    # return [int(a) for a in str(num)]

    # 2) A better approach is to propagate carries. The time complexity is O(n)
    # and space complexity is O(1).
    carry = True
    for idx in reversed(range(len(A))):
        if carry and A[idx] == 9:
            A[idx] = 0
        elif carry:
            A[idx] += 1
            carry = False

    if carry:
        # There's a carry. A slick way to do this is to change the first entry
        # to 1, as the previous entry must have been 9. Then append 0.
        A[0] = 1
        A.append(0)

    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_increment.py", "int_as_array_increment.tsv", plus_one
        )
    )
