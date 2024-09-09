import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

""" 15.1 """


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    """https://www.youtube.com/watch?v=boS4N1_TLBk"""

    def _compute(
        num_rings_to_move: int, start_peg: int, end_peg: int, use_peg: int
    ) -> None:

        # Only move the rings if there is a ring to move.
        if num_rings_to_move > 0:
            _compute(num_rings_to_move - 1, start_peg, use_peg, end_peg)
            # Gather the results at this stage as a move has just been made.
            result.append([start_peg, end_peg])
            _compute(num_rings_to_move - 1, use_peg, end_peg, start_peg)

    result: List[List[int]] = []
    _compute(num_rings, 0, 1, 2)

    return result


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure(
                "Illegal move from {} to {}".format(
                    pegs[from_peg][-1], pegs[to_peg][-1]
                )
            )
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "hanoi.py", "hanoi.tsv", compute_tower_hanoi_wrapper
        )
    )
