from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    """
    Multiply the two arrays, using basic elementary multiplication.

    i.e. [1,3,4] & [2,3] = [3,0,8,2]

    """
    # First, set the signs.
    sign = -1 if (num1[0] < 0) != (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    # From a space perspective, add incrementally rather than at the end.
    # result = [0,0,0,0,0]
    result = [0] * (len(num1) + len(num2))
    # Reverse the range of i -> [2,1,0]
    for i in reversed(range(len(num1))):
        # Reverse j -> [1,0]
        for j in reversed(range(len(num2))):
            # First set the result at a +1 index.
            result[i + j + 1] += num1[i] * num2[j]
            # result = [1,12,0,0,0]
            result[i + j] += result[i + j + 1] // 10
            # result = [1,2,0,0,0]
            result[i + j + 1] %= 10

    # Remove any leading zeros, by getting the first index at which it is not
    # zero
    result = result[
        next((i for i, x in enumerate(result) if x != 0), len(result)) :
    ] or [0]

    return [sign * result[0]] + result[1:]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_multiply.py", "int_as_array_multiply.tsv", multiply
        )
    )
