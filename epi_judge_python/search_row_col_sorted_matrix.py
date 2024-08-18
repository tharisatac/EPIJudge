from typing import List

from test_framework import generic_test

""" 11.6 """


def matrix_search(A: List[List[int]], x: int) -> bool:
    """Find if x is in A"""

    row = 0
    col = len(A[0]) - 1

    while row < len(A) and col >= 0:
        curr = A[row][col]
        if x == curr:
            return True
        elif x > curr:
            row += 1
        else:
            col -= 1

    return False


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_row_col_sorted_matrix.py",
            "search_row_col_sorted_matrix.tsv",
            matrix_search,
        )
    )
