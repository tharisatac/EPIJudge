from typing import List
import collections

from test_framework import generic_test

""" 18.3 """


def fill_surrounded_regions(board: List[List[str]]) -> None:
    """Fill surrounded regions."""

    n, m = len(board), len(board[0])

    # Collect the boundary cells
    q = collections.deque(
        [(i, 0) for i in range(n)]
        + [(i, m - 1) for i in range(n)]  # First and last column
        + [(0, j) for j in range(m)]
        + [(n - 1, j) for j in range(m)]  # First and last row
    )

    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and board[x][y] == "W":
            # Flip it to equal t
            board[x][y] = "T"
            q.extend([(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)])

    board[:] = [["B" if c != "T" else "W" for c in row] for row in board]


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "matrix_enclosed_regions.py",
            "matrix_enclosed_regions.tsv",
            fill_surrounded_regions_wrapper,
        )
    )
