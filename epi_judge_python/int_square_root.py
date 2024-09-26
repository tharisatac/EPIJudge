from test_framework import generic_test


def square_root(k: int) -> int:
    """Find the the largest integer whose square is equal to or smaller than k"""
    left, right = 0, k

    # When left == right, this ensures the mid-point is still evaluated. Take
    # 16 as an example.
    # 0, 16
    # 0, 7
    # 4, 7
    # 4, 4
    # If you do not do left == right here, left will be 4 and you will return
    # 3, which is wrong. This means that 4 isn't evaluated!
    while left <= right:
        m = (left + right) // 2
        m_sq = m * m
        # If m_sq == k, then m is the exact candidate. We take left up by 1
        # so that we can take 1 away from it at the end (and left will be
        # greater than right)
        if m_sq <= k:
            left = m + 1
        elif m_sq > k:
            right = m - 1

    return left - 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_square_root.py", "int_square_root.tsv", square_root
        )
    )
