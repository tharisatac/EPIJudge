from test_framework import generic_test
from math import ceil, floor, log10


def is_palindrome_number(x: int) -> bool:
    """Check if a number is palindromic"""

    # 1) A brute force approach is to iterate through each digit and compare it
    # to its opposite member.

    # num = ceil(len(str(abs(x))) / 2)
    # digits = str(x)
    # for i in range(num):
    #     if digits[i] != digits[-(i + 1)]:
    #         return False

    # 2) The better approach is to once again, use maths. The number of digits
    # in x, is floor(log10(x)) + 1. You can prove this because log10(x) is what
    # gives you the highest number of 10.

    if x <= 0:
        # Negative integers are non-palindromic
        return x == 0

    num_digits = floor(log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)

    for _ in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False

        # Remove the most significant digit. This gives you the remainder
        # remember. So 3278 mod 10000 = 278
        x %= msd_mask

        # Remove the least significant digit. This is a floor division.
        # So 278 // 10 = 27
        x //= 10

        # Update the msd_mask.
        msd_mask //= 100

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_number_palindromic.py",
            "is_number_palindromic.tsv",
            is_palindrome_number,
        )
    )
