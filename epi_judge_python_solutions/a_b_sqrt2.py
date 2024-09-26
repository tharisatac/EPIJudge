import math
from typing import List

# import bintrees

from test_framework import generic_test

# These numbers have very interesting property, and people called it ugly numbers. It is also called quadratic integer rings.


class Number:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


""" 14.7 """


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:

    # # Initial for 0 + 0 * sqrt(2).
    # candidates = bintrees.RBTree([(Number(0, 0), None)])

    # result: List[float] = []
    # while len(result) < k:
    #     next_smallest = candidates.pop_min()[0]
    #     result.append(next_smallest.val)
    #     # Adds the next two numbers derived from next_smallest.
    #     candidates[Number(next_smallest.a + 1, next_smallest.b)] = None
    #     candidates[Number(next_smallest.a, next_smallest.b + 1)] = None
    # return result

    cand = [Number(0, 0)]
    i = j = 0

    for _ in range(1, k):
        cand_i_plus_1 = Number(cand[i].a + 1, cand[i].b)
        cand_j_plus_sqrt2 = Number(cand[j].a, cand[j].b + 1)

        if cand_i_plus_1 < cand_j_plus_sqrt2:
            cand.append(cand_i_plus_1)
            i += 1

        if cand_j_plus_sqrt2 < cand_i_plus_1:
            cand.append(cand_j_plus_sqrt2)
            j += 1

        if cand_j_plus_sqrt2 == cand_i_plus_1:
            cand.append(cand_i_plus_1)
            i += 1
            j += 1

    return [a.val for a in cand]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "a_b_sqrt2.py", "a_b_sqrt2.tsv", generate_first_k_a_b_sqrt2
        )
    )
