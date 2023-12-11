from test_framework import generic_test


def reverse(x: int) -> int:
    """Reverse the digits."""
    # 1) Brute force method: convert to string then reverse
    # if x > 0:
    # return int(str(x)[::-1])
    # else:
    # return -1 * int(str(x)[:0:-1])

    # 2) Use mod 10.
    result, x_remaining = 0, abs(x)

    while x_remaining:
        result = result * 10 + x_remaining % 10
        # Use floor division, because we just want the next number!!
        x_remaining //= 10

    return result if x > 0 else -result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_digits.py", "reverse_digits.tsv", reverse
        )
    )
