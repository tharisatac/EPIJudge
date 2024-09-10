from typing import List

from test_framework import generic_test

""" 15.3 """


def n_queens(n: int) -> List[List[int]]:
    """Find all non-attacking placements of n-queens"""

    def _solve(row):
        if row == n:
            # We've now solved it for theses sets of columns.
            return result.append(col_placement.copy())

        for col in range(n):
            if all(
                abs(c - col) not in (0, row - i)
                for i, c in enumerate(col_placement[:row])
            ):
                col_placement[row] = col
                _solve(row + 1)

        return

    result: List[List[int]] = []
    col_placement = [0] * n
    _solve(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("n_queens.py", "n_queens.tsv", n_queens, comp))
