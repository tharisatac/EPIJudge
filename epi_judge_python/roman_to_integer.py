from test_framework import generic_test
import functools

""" 6.8 """


def roman_to_integer(s: str) -> int:
    """Convert a Roman numeral to an integer."""

    T = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # return functools.reduce(
    # lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
    # reversed(range(len(s) - 1)),
    # T[s[-1]],
    # )

    result = T[s[-1]]

    for i in reversed(range(len(s) - 1)):
        if T[s[i]] < T[s[i + 1]]:
            result -= T[s[i]]
        else:
            result += T[s[i]]

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", "roman_to_integer.tsv", roman_to_integer
        )
    )
