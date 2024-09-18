from test_framework import generic_test
import functools

""" 16.2 """


def levenshtein_distance(A: str, B: str) -> int:
    """Compute the levenshtein distance"""

    @functools.lru_cache(None)
    def _compute(a, b):
        """Helper function"""

        if a < 0:
            # a is empty, return B's characters
            return b + 1
        if b < 0:
            # b is empty, so delete all of A's characters
            return a + 1

        if A[a] == B[b]:
            # they're the same, so go to the next character
            return _compute(a - 1, b - 1)

        susbitute_last = _compute(a - 1, b - 1)
        add_last = _compute(a - 1, b)
        remove_last = _compute(a, b - 1)

        return 1 + min(susbitute_last, add_last, remove_last)

    return _compute(len(A) - 1, len(B) - 1)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "levenshtein_distance.py", "levenshtein_distance.tsv", levenshtein_distance
        )
    )
