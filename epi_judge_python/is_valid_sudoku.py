from typing import List
import math

from test_framework import generic_test

""" 5.17 Sudoku Checker """


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    """
    Check if a partially filled soduku array is valid.

    [[9,0,0,0,3,2,1,0,0],
     [8,7,1,0,0,5,0,0,0]
     .
     .
     .
     ]

    """

    def has_duplicate(block):
        """Checks if a number appears in a block more than once."""
        nums = [x for x in block if x != 0]
        return len(nums) != len(set(nums))

    n = len(partial_assignment)
    # Check row and col constraints
    for i in range(n):
        if has_duplicate(partial_assignment[i]) or has_duplicate(
            [partial_assignment[j][i] for j in range(n)]
        ):
            return False

    # Check region constraints
    region_size = int(math.sqrt(n))
    return all(
        not has_duplicate(
            [
                partial_assignment[a][b]
                for a in range(region_size * I, region_size * (I + 1))
                for b in range(region_size * J, region_size * (J + 1))
            ]
        )
        for I in range(region_size)
        for J in range(region_size)
    )

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_sudoku.py", "is_valid_sudoku.tsv", is_valid_sudoku
        )
    )
