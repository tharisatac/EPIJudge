import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

""" 15.11 """


def gray_code(num_bits: int) -> List[int]:
    """Computes a gray code"""

    def directed_gray_code(history):

        def differs_by_one_bit(x, y):
            # bit_diff ensures that we are not comparing two identical numbers (where x ^ y would be 0).
            bit_diff = x ^ y
            # not (bit_diff & (bit_diff - 1)) ensures that bit_diff is a power of 2, which tells us that x and y differ by exactly one bit.
            return bit_diff and not (bit_diff & (bit_diff - 1))

        if len(result) == 1 << num_bits:
            return differs_by_one_bit(result[0], result[-1])

        # Now do the back tracking
        for i in range(num_bits):
            previous_code = result[-1]
            candidate = previous_code ^ (1 << i)
            if candidate not in history:
                history.add(candidate)
                result.append(candidate)
                if directed_gray_code(history):
                    return True

                history.remove(candidate)
                del result[-1]

    result = [0]
    directed_gray_code(set([0]))
    return result


def differ_by_1_bit(a, b):
    x = a ^ b
    if x == 0:
        return False
    while x & 1 == 0:
        x >>= 1
    return x == 1


@enable_executor_hook
def gray_code_wrapper(executor, num_bits):
    result = executor.run(functools.partial(gray_code, num_bits))

    expected_size = 1 << num_bits
    if len(result) != expected_size:
        raise TestFailure(
            "Length mismatch: expected "
            + str(expected_size)
            + ", got "
            + str(len(result))
        )
    for i in range(1, len(result)):
        if not differ_by_1_bit(result[i - 1], result[i]):
            if result[i - 1] == result[i]:
                raise TestFailure("Two adjacent entries are equal")
            else:
                raise TestFailure("Two adjacent entries differ by more than 1 bit")

    uniq = set(result)
    if len(uniq) != len(result):
        raise TestFailure(
            "Not all entries are distinct: found "
            + str(len(result) - len(uniq))
            + " duplicates"
        )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "gray_code.py", "gray_code.tsv", gray_code_wrapper
        )
    )
