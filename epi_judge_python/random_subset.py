import functools
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient,
    check_sequence_is_uniformly_random,
    compute_combination_idx,
    run_func_with_retries,
)
from test_framework.test_utils import enable_executor_hook

""" 5.15 Random subset. """


def random_subset(n: int, k: int) -> List[int]:
    """Create a random subset of k."""

    # Create a hash table to store values.
    change_elements: dict[int, int] = {}
    for i in range(k):
        # Generate a random index between i and n-1, inclusive.
        rand_idx = random.randrange(i, n)
        # Return the value in the dictionary if one exists.
        rand_idx_mapped = change_elements.get(rand_idx, rand_idx)
        # Get the element at the current index if one exists.
        i_mapped = change_elements.get(i, i)

        # Assign the elements.
        change_elements[rand_idx] = i_mapped
        change_elements[i] = rand_idx_mapped

    return [change_elements[i] for i in range(k)]


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes,
            0.01,
        )

    run_func_with_retries(functools.partial(random_subset_runner, executor, n, k))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "random_subset.py", "random_subset.tsv", random_subset_wrapper
        )
    )
