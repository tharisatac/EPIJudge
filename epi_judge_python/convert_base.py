from test_framework import generic_test
import string, functools


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    """Convert between bases."""

    def construct_from_base(num_as_int, base):
        """Use dynamic programming instead of recursion!"""
        result = []

        while num_as_int > 0:
            result.append(string.hexdigits[num_as_int % base].upper())
            num_as_int //= base

        return "".join(result[::-1]) if result else "0"

    # 1) Convert to a decimal base. This is the most basic and easiest one.
    is_negative = False
    if num_as_string[0] == "-":
        is_negative = True

    # functools.reduce is great for accumulation!
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:],
        0,
    )

    return ("-" if is_negative else "") + (
        "0" if num_as_int == 0 else construct_from_base(num_as_int, b2)
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "convert_base.py", "convert_base.tsv", convert_base
        )
    )
