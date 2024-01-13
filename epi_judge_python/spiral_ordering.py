from typing import List

from test_framework import generic_test

""" 5.18 Spiral Ordering """


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    """Returns the matrix in spiral order. This can use an iterative algorithm"""

    spiral_ordering: list[int] = []

    def matrix_in_layer_clockwise(offset):
        """Unwraps the square matrix by the offset provided."""
        # Check if it's an odd matrix. This is an edge case where there's a
        # centre piece.
        if offset == len(square_matrix) - offset - 1:
            spiral_ordering.append(square_matrix[offset][offset])
            return

        # Top row
        spiral_ordering.extend(square_matrix[offset][offset : -1 - offset])

        # Downward, non-reversed
        spiral_ordering.extend(
            [
                square_matrix[i][-1 - offset]
                for i in range(offset, len(square_matrix) - offset - 1)
            ]
        )

        # Bottom row, reversed.
        spiral_ordering.extend(
            square_matrix[-1 - offset][-1 - offset : offset : -1],
        )

        # Upwards, reversed
        spiral_ordering.extend(
            [
                square_matrix[i][offset]
                for i in range(-1 - offset, -(len(square_matrix) - offset), -1)
            ]
        )

    for i in range(len(square_matrix) + 1 // 2):
        matrix_in_layer_clockwise(i)

    return spiral_ordering


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spiral_ordering.py", "spiral_ordering.tsv", matrix_in_spiral_order
        )
    )
