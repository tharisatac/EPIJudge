import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple(
    "DuplicateAndMissing", ("duplicate", "missing")
)

""" 11.10 """


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    """Find the duplicate and the missing integer"""
    # Find m XOR t.

    # Reduce a list into bits
    # When we do enumerate, that gives us two arrays:
    # An array from 0 to n - 1, i.e. [0,1,2,3,4,5]
    # And the actual values, i.e. [5,4,3,3,0,1]
    # When we do an XOR, any value that is the same will be removed.
    # therefore what's left is 2 XOR 3 or 2 ^ 3
    miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)

    # We now know that 2 XOR 3 = miss_xor_dup. It's impossible to figure out
    # which is which right now. BUT, we know that 2 and 3 MUST differ somewhere
    # otherwise miss_xor_dup will be 0. Therefore find a bit where that differs.
    # Isolate the lowest set bit.
    differ_bit = miss_xor_dup & (~(miss_xor_dup - 1))
    miss_or_dup = 0

    # Now find the numbers where the differ_bit_th bit is 1.

    # Why this works:
    # Remember:
    # An array from 0 to n - 1, i.e. [0,1,2,3,4,5]
    # And the actual values, i.e. [5,4,3,3,0,1]
    # The lowest set bit of 2 XOR 3 (i.e. (010) XOR (011) = (001))

    # Isolate all the numbers with this bit
    # You get [1,3,5] from the first array
    # You get [5,3,3,1] from the second array. i.e. one of m or t will be
    # isolated here whereas the other one won't
    # We will get back 3.
    for i, a in enumerate(A):
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a

    return (
        DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_xor_dup)
        if miss_or_dup in A
        else DuplicateAndMissing(miss_or_dup ^ miss_xor_dup, miss_or_dup)
    )


def res_printer(prop, value):
    def fmt(x):
        return "duplicate: {}, missing: {}".format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED, PropertyName.RESULT) else value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            "find_missing_and_duplicate.tsv",
            find_duplicate_missing,
            res_printer=res_printer,
        )
    )
