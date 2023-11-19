from test_framework import generic_test

from typing import Dict
import sys
import math

""" 4.3 Reverse Bits """


def swap_bits(x: int, i: int, j: int) -> int:
    """
    Swaps bits in the i-th and j-th index. Exactly the same as swap_bits.py
    """
    # Isolate the i-th and j-th bits. If they're the same, do nothing! Otherwise
    # flip them.
    if not ((x >> i) & 1 == (x >> j) & 1):
        # 1 << i | 1 << j: The | operator performs a bitwise OR operation
        # between the results of the left shift operations from steps 1 and 2.
        # It combines the bits of the two numbers, resulting in a new binary
        # number. For example, if i is 3 and j is 2, 1 << 3 | 1 << 2 would
        # result in the binary number 1100, which is 12 in decimal.
        x ^= 1 << i | 1 << j
    return x


def _reverse_hash_table(bit_size: int) -> Dict[int, int]:
    """Build up a hash table of a 'bit_size' int and its reverse value"""
    # Either 0,1,3,7,15,31,63

    # 1) Normal.
    hash_table = {}
    for i in range(int(2 ** (bit_size)) / 2):
        if i not in hash_table:
            x = i
            for j in range(int(bit_size / 2)):
                x = swap_bits(x, j, bit_size - 1 - j)

            hash_table[i] = x
            hash_table[x] = i

    return hash_table


MAX_SIZE = 64
MASK_SIZE = int(MAX_SIZE / 4)  # Each key in the lookup table is 16 bits
LOOKUP_TABLE = _reverse_hash_table(MASK_SIZE)


def reverse_bits(x: int) -> int:
    """Reverses a 64-bit unsigned integer."""

    # 1) Brute-force algorithm -> O(n)
    # Iterate through the 32 least significant bits &
    # swap it with its opposing bit. This can utilize what is done in
    # swap_bits.py
    INT_SIZE = 63  # 63 (because the index starts at 0)

    # Range is 32 because it is 0 -> 31, 32 is excluded. You only want to go up
    # to half way.
    # for i in range(int((INT_SIZE + 1) / 2)):
    #     x = swap_bits(x, i, INT_SIZE - i)
    # return x

    # 2) Use a hash table (similar to 4.1, solution 3). -> O(n/k) where k is the
    # size each word.
    # hash_table = _reverse_hash_table(15)
    # bit_mask = 0xFFFF
    # shift = 16
    bitmask = 0xFFFF  # F is 1111
    return (
        LOOKUP_TABLE[x & bitmask] << (MASK_SIZE * 3)
        | LOOKUP_TABLE[(x >> MASK_SIZE) & bitmask] << (MASK_SIZE * 2)
        | LOOKUP_TABLE[(x >> (2 * MASK_SIZE)) & bitmask] << (MASK_SIZE * 1)
        | LOOKUP_TABLE[(x >> (3 * MASK_SIZE)) & bitmask]
    )

    result = ""
    for i in range(3, -1, -1):
        result += str(LOOKUP_TABLE[(x >> (i * 16)) & bitmask])

    return int(result)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_bits.py", "reverse_bits.tsv", reverse_bits
        )
    )
