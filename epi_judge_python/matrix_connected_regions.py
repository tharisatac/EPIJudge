from typing import List
import collections

from test_framework import generic_test

""" 18.2 """


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    """Do BFS"""
    colour = image[x][y]
    q = collections.deque([(x, y)])

    image[x][y] = not image[x][y]
    while q:
        x, y = q.popleft()
        for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
            if (
                0 <= next_x < len(image)
                and 0 <= next_y < len(image[next_x])
                and image[next_x][next_y] == colour
            ):
                # Flip the colour
                image[next_x][next_y] = not image[next_x][next_y]
                q.append((next_x, next_y))


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "matrix_connected_regions.py", "painting.tsv", flip_color_wrapper
        )
    )
