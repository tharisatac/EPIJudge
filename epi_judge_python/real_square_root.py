from test_framework import generic_test
import math

""" 11.5 """


def square_root(x: float) -> float:
    """Computes the square root of x."""
    # If x < 1, the square root of x will be greater than x.
    # i.e. square root of 1/4 is 1/2.
    if x < 1:
        left, right = x, 1
    else:
        left, right = 1, x

    while not math.isclose(left, right):
        m = 0.5 * (left + right)
        m_sq = m * m

        if m_sq > x:
            right = m
        else:
            left = m

    # The complexity is O(log(x/s)) where s is the significance.
    # Look into Newton-Raphson?
    return left


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "real_square_root.py", "real_square_root.tsv", square_root
        )
    )
