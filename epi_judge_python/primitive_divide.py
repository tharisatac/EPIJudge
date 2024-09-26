from test_framework import generic_test


def divide(x: int, y: int) -> int:
    """
    Primitive divide. Find the quotient (i.e. x/y, not the remainder), but only
    using addition, subtraction and shifting operators.

    Remember: the quotient x/y means, how many times does y go into x.
    """
    # 1) Brute force method -> x/y
    # - Subtract y from x until the remainder is less than y. This is extremely
    # slow.
    # quotient = 0
    # while x >= y:
    # x -= y
    # quotient += 1

    # 2) A better method is to do more, every time we subtract.
    # We find that (2^k)y <= x, will still allow us to divide into x. And this
    # is guaranteed to divide x by 2 every time!
    # The reason for (2^k)y is because it allows for shifting operations.
    #
    # Instead of finding k everytime, find it the first time. And then we know
    # that the next k must be less than the previous k. So do k-1 and so on...

    # Assuming a 32-bit system.
    quotient = 0
    k = 32

    two_k_y = y << k

    while x >= y:
        while two_k_y > x:
            two_k_y >>= 1
            k -= 1

        quotient += 1 << k  # Same as adding 2^k
        x -= two_k_y

    return quotient


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "primitive_divide.py", "primitive_divide.tsv", divide
        )
    )
