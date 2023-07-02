from test_framework import generic_test

""" 4.1.1 Computing the Parity of a Word """


def compute_lookup_table(l: int) -> dict[str, int]:
    """
    Computes a lookup table based on the passed-in length.

    Arguments:
        l: The width of the word for which results are cached.

    """
    
    def _compute_parity(x: int) -> int:
        """ Computes the parity of a word. """
    
    max_num = 2 ^ l
    curr = 0
    table = {}
    while curr <= max_num:
        table[]
    # while x:
    #   result ^= 1
    #   x &= x - 1
    # return result


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
    result = 0
    while x:
      result ^= 1
      x &= x - 1  # Drops the lowest set bit
    return result

    # 3) Look up table - O(n/L) where n is the length of the word and L is the
    #                    the size of the window.
    # i) Compute the lookup table.


if __name__ == "__main__":
    exit(generic_test.generic_test_main("parity.py", "parity.tsv", parity))
