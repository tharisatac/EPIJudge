from test_framework import generic_test


def square_root(k: int) -> int:
    """Find the the largest integer whose square is equal to or smaller than k"""
    left, right = 0, k

    # Whilst there's an interval. It's less than or equal to because if it's
    # equal, we can still keep going.
    while left <= right:
        m = (left + right) // 2
        m_sq = m * m
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
