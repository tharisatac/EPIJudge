from typing import Set

import collections
import string
from test_framework import generic_test

""" 18.7 """


def transform_string(D: Set[str], s: str, t: str) -> int:
    """Transform the String"""

    StringWithDistance = collections.namedtuple(
        "StringWithDistance", ("candidate_string", "distance")
    )
    q = collections.deque([StringWithDistance(s, 0)])
    # Mark s as visited
    D.remove(s)

    while q:
        f = q.popleft()
        # Return if we find a match
        if f.candidate_string == t:
            return f.distance

        # Trie all the possible transformations
        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase:
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1 :]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))

    return -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_transformability.py",
            "string_transformability.tsv",
            transform_string,
        )
    )
