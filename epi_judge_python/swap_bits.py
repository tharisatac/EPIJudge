from test_framework import generic_test

""" 4.2 Swap bits """


def swap_bits(x, i, j):
    """Swap bits at the ith and jth position for word x"""

    # 1) Find the value at each index - O(1)
    # Use a bitmask to isolate the i-th and j-th bit.
    # If the values are the same, we don't actually need to swap.
    # Else, flip the bits.

    # No need to swap if the values are the same.
    if not ((x >> i) & 1 == (x >> j) & 1):
        # Flip the indexed bit. This is done using an XOR.
        x ^= 1 << i | 1 << j
    return x


if __name__ == "__main__":
    exit(generic_test.generic_test_main("swap_bits.py", "swap_bits.tsv", swap_bits))
