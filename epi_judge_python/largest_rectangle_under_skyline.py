from typing import List

from test_framework import generic_test

""" 17.8 """


def calculate_largest_rectangle(heights: List[int]) -> int:
    """Computes the largest rectangle in a skyline"""

    # We store the set of the active pillar sets.
    pillar_indices: List[int] = []

    # Store the maximum rectangular area.
    max_rectangle_area = 0

    # By appending [0] to heights, we can uniformly handle the computation of
    # the rectangle area here.
    for i, h in enumerate(heights + [0]):
        # We need to pop the building that is greater than the current height as
        # it is now blocked and no longer in consideration.
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1

            max_rectangle_area = max(max_rectangle_area, height * width)

        pillar_indices.append(i)

    return max_rectangle_area


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "largest_rectangle_under_skyline.py",
            "largest_rectangle_under_skyline.tsv",
            calculate_largest_rectangle,
        )
    )
