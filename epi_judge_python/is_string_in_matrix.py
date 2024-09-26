from typing import List

import functools

from test_framework import generic_test

""" 16.5 """


def is_pattern_contained_in_grid(grid: List[List[int]], pattern: List[int]) -> bool:
    """Is a pattern contained within a grid?"""

    @functools.lru_cache
    def is_patterin_suffix_in_grid(x, y, offset):
        """Helper function to compute whether the pattern suffix is in the grid"""

        if len(pattern) == offset:
            # The pattern is empty and thus is in the grid.
            return True

        # Early return if x and y are no longer in the grid (as there's nothing
        # left to check) or the pattern doesn't match the current entry.
        if (not (0 <= x < len(grid) and 0 <= y < len(grid[x]))) or pattern[
            offset
        ] != grid[x][y]:
            return False

        return any(
            is_patterin_suffix_in_grid(*next_xy, offset + 1)
            for next_xy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        )

    return any(
        is_patterin_suffix_in_grid(i, j, 0)
        for i in range(len(grid))
        for j in range(len(grid[i]))
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_in_matrix.py",
            "is_string_in_matrix.tsv",
            is_pattern_contained_in_grid,
        )
    )
