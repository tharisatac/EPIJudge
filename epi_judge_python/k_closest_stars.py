import functools
import math
import heapq
from typing import Iterator, List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

""" 10.4 """


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: "Star") -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    """
    Use a Max Heap to find the k-closest stars

    The time complexity is O(nlogk) because it takes O(logk) to add elements
    to a max heap as insertion takes O(logk). We do this n times for n stars.
    """

    max_heap: list[tuple[float, Star]] = []

    for star in stars:
        # Add each star to the max heap. If the number of stars exceeds k,
        # remove the last star.
        # Use the negative distance as it is a max-heap.
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [s[1] for s in heapq.nlargest(k, max_heap)]


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d) for s, d in zip(sorted(output), expected_output)
    )


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars), k))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_closest_stars.py",
            "k_closest_stars.tsv",
            find_closest_k_stars_wrapper,
            comp,
        )
    )
