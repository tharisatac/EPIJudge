from test_framework import generic_test

""" 4.4 Find a closest integer with the same weight """


def closest_int_same_bit_count(x: int) -> int:
    """
    Find the closest two integers with the same weight for a 64-bit integer.
    """
    # 1) Swap the two consecutive rightmost bits that differ
    bits = 64

    for i in range(bits - 1):
        if (x >> i) & 1 != (x >> (i + 1) & 1):
            # Swap the bits
            x ^= (1 << i) | (1 << (i + 1))
            return x

    raise ValueError("All 0s or 1s")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "closest_int_same_weight.py",
            "closest_int_same_weight.tsv",
            closest_int_same_bit_count,
        )
    )
