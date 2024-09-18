from test_framework import generic_test
import functools

""" 16.3 """


def number_of_ways(n: int, m: int) -> int:
    """Find the number of ways to get to the bottom right of an nxm array"""

    @functools.lru_cache(None)
    def _compute(x, y):
        if x == y == 0:
            return 1

        ways_top = 0 if x == 0 else _compute(x - 1, y)
        ways_left = 0 if y == 0 else _compute(x, y - 1)

        return ways_top + ways_left

    return _compute(n - 1, m - 1)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_traversals_matrix.py",
            "number_of_traversals_matrix.tsv",
            number_of_ways,
        )
    )
