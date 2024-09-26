from test_framework import generic_test
import collections

""" 12.2 """


def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    """Can you construct this letter form the magazine?"""

    letters = collections.defaultdict(int)
    for i in magazine_text:
        letters[i] += 1

    for j in letter_text:
        if letters[j] == 0:
            return False
        else:
            letters[j] -= 1

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_anonymous_letter_constructible.py",
            "is_anonymous_letter_constructible.tsv",
            is_letter_constructible_from_magazine,
        )
    )
