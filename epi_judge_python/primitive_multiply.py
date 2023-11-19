from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    """Multiply two nonnegative integers using bitwise operators"""

    # Multiply is simple.
    # 1) Iterate through x, with variable k
    # 2) When the bit is 1, shift y by the k index
    # 3) Add all the numbers together at the end.
    #   (Bitwise addition involves adding each bit and 'carrying the 1')

    def _add(a, b):
        """
        This works be:
            1) ^: XORs each number together
            2) &: Only two 1's will result in 1. This is shifted left (as a carry)
            3) Continue until there are no more carries.

        5: 101
        3: 011

        8: 1000

         ^      &     << 1
        101    101
        011    011
        ---  , ---  ,
        110(a) 001    010(b)

        & repeat
        """
        return a if b == 0 else _add((a ^ b), (a & b) << 1)

    running_sum = 0
    while x:
        if x & 1:
            # Shift y by the index
            running_sum = _add(running_sum, y)
        x, y = x >> 1, y << 1

    return running_sum


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "primitive_multiply.py", "primitive_multiply.tsv", multiply
        )
    )
