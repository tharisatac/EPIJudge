import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple("Item", ("weight", "value"))

""" 16.6 """


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    """The knapsack problem."""

    @functools.lru_cache(None)
    def _optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            # Nothing left to compute.
            return 0

        without_curr_item = _optimum_subject_to_item_and_capacity(
            k - 1, available_capacity
        )

        with_curr_item = (
            0
            if available_capacity < items[k].weight
            else items[k].value
            + _optimum_subject_to_item_and_capacity(
                k - 1, available_capacity - items[k].weight
            )
        )

        return max(without_curr_item, with_curr_item)

    return _optimum_subject_to_item_and_capacity(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "knapsack.py", "knapsack.tsv", optimum_subject_to_capacity_wrapper
        )
    )
