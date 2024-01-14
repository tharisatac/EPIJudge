from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string

""" 6.1 String to Integer Conversion """


def int_to_string(x: int) -> str:
    """Converts an integer to string without using any Python libraries."""
    # As we can't used python libraries like int() or str(). This must be done
    # in a step by step process. One digit at a time.

    is_negative = False
    if x < 0:
        is_negative = True
        x = -x

    s = []
    while True:
        s.append(chr(ord("0") + x % 10))
        x //= 10

        if x == 0:
            break

    return ("-" if is_negative else "") + "".join(reversed(s))


def string_to_int(s: str) -> int:
    """Converts a string to an integer without using int()."""

    running_sum: int = 0

    for c in s[s[0] in "+-" :]:
        running_sum = running_sum * 10 + string.digits.index(c)

    return (-1 if s[0] == "-" else 1) * running_sum


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )
