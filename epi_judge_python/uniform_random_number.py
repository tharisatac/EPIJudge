import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random,
    run_func_with_retries,
)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    """Generates a random number between the lower and upper bounds."""
    # Add 1 as it's inclusive. So range [3,7], would be 5 as it's 3,4,5,6,7.
    num_outcomes = upper_bound - lower_bound + 1

    while True:
        result = 0
        i = 0
        while (i << 1) < num_outcomes:
            # This affectively appends the bit to the end of result
            result = (result << 1) | zero_one_random()
            i += 1

        if result < num_outcomes:
            # Only break out of the while loop if the result satisfies the
            # criteria.
            break

    return result + lower_bound


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda: [uniform_random(lower_bound, upper_bound) for _ in range(100000)]
        )

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1, 0.01
        )

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound, upper_bound)
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "uniform_random_number.py",
            "uniform_random_number.tsv",
            uniform_random_wrapper,
        )
    )
