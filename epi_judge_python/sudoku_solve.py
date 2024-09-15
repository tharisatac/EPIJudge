import copy
import functools
import itertools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

""" 15.10 """


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    """Solve a soduku using backtracking!"""

    def _solve_partial_sudoku(i, j):

        if i == len(partial_assignment):
            i = 0
            j += 1  # Increment the column (go to the next row)

            if j == len(partial_assignment):
                # We've now reached the end of the grid
                return True

        # Skip the non-entry array:
        if partial_assignment[i][j] != empty_entry:
            # Move to the next entry in the row
            return _solve_partial_sudoku(i + 1, j)

        def is_valid(i, j, val):
            # Check the column constraints
            if any(
                val == partial_assignment[k][j] for k in range(len(partial_assignment))
            ):
                return False

            # Check the row constraints
            if val in partial_assignment[i]:
                return False

            # Check the box constraints
            region_size = int(math.sqrt(len(partial_assignment)))
            I = i // region_size
            J = j // region_size

            return not any(
                val == partial_assignment[region_size * I + a][region_size * J + b]
                for a, b in itertools.product(range(region_size), repeat=2)
            )

        for val in range(1, len(partial_assignment) + 1):
            if is_valid(i, j, val):
                partial_assignment[i][j] = val
                if _solve_partial_sudoku(i + 1, j):
                    return True

        partial_assignment[i][j] = empty_entry
        return False

    empty_entry = 0
    return _solve_partial_sudoku(0, 0)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure("Cell left uninitialized")
        if x < 0 or x > len(seq):
            raise TestFailure("Cell value out of range")
        if x in seen:
            raise TestFailure("Duplicate value in section")
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j]
        for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure("Initial cell assignment has been changed")

    for br, sr in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure("Initial cell assignment has been changed")
        for bcell, scell in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure("Initial cell assignment has been changed")

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sudoku_solve.py", "sudoku_solve.tsv", solve_sudoku_wrapper
        )
    )
