from test_framework import generic_test

""" 4.1 Computing the Parity of a Word """

from math import floor


def compute_lookup_table(l: int) -> dict[str, int]:
    """
    Computes a lookup table based on the passed-in mask_size.

    :arguments:
        l: The mask size.

    :returns:
        A precomputed lookup table where each key is a bitword and the value its
        parity.
    """

    max_num = 2**l
    table = {0: 0}

    for i in range(1, max_num):
        # 6) Count the number of 1s then modulo 2 to get odd or even.
        table[i] = (table[i >> 1] + (i & 1)) % 2

    return table


MAX_SIZE = 64
MASK_SIZE = int(MAX_SIZE / 4)  # Each key in the lookup table is 16 bits
LOOKUP_TABLE = compute_lookup_table(MASK_SIZE)


def parity(x: int) -> int:
    """
    Computes the parity of a word.

    A word with an odd number of 1's has a parity of 1.
    """

    # 1) Brute force - O(n) where n is the length of the word
    # In each loop:
    # - Use bitwise XOR to collect the number of 1s
    # - Right shift x each bit at a time using
    #
    # result = 0
    # while x:
    #     result ^= x & 1
    #     x >>= 1

    # 2) Erase the lowest set bit - O(k) where k is the number of set bits
    # In each loop:
    # - XOR to result.
    # - Drop the lowest set bit.
    #
    # result = 0
    # while x:
    #     result ^= 1
    #     x &= x - 1  # Drops the lowest set bit
    # return result

    # 3) Look up table - O(n/L) where n is the length of the word and L is the
    #                    the size of the window.
    # i)  Compute the lookup table.
    # ii) Use look up table by calculating the parity of each non-overlapping
    #     group
    bitmask = 0xFFFF  # F is 1111
    return (
        LOOKUP_TABLE[x & bitmask]
        ^ LOOKUP_TABLE[(x >> MASK_SIZE) & bitmask]
        ^ LOOKUP_TABLE[(x >> (2 * MASK_SIZE)) & bitmask]
        ^ LOOKUP_TABLE[(x >> (3 * MASK_SIZE)) & bitmask]
    )

    # 4) Use associativity - O(log(n)) where n is the length of the word
    # The XOR of a group of bits is its parity.
    # half = int(MAX_SIZE / 2)
    # while half > 0:
    #     x ^= x >> half
    #     half = floor(half / 2)
    # return x & 0x1


if __name__ == "__main__":
    exit(generic_test.generic_test_main("parity.py", "parity.tsv", parity))
