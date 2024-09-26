from typing import List

from test_framework import generic_test

""" 12.5 """


def find_nearest_repetition(paragraph: List[str]) -> int:
    """Find the nearest repeated entries"""

    words: dict[str, int] = {}
    nearest_distance: float = float("inf")
    for i, word in enumerate(paragraph):
        if word in words:
            idx = words[word]
            nearest_distance = min(i - idx, nearest_distance)
        words[word] = i

    return int(nearest_distance) if nearest_distance != float("inf") else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "nearest_repeated_entries.py",
            "nearest_repeated_entries.tsv",
            find_nearest_repetition,
        )
    )
