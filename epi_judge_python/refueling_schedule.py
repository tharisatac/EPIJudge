import functools
import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20

""" 17.6"""


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    """Find the ample city."""
    remaining_gallons = 0
    CityAndGas = collections.namedtuple("CityAndGas", ("city", "gas"))

    num_cities = len(gallons)

    city_and_gas = CityAndGas(0, float("inf"))
    for i in range(num_cities):
        remaining_gallons += gallons[i] - distances[i] // MPG
        # We want to find the smallest amout of gas before we need to refuel.
        # So it is the next city (after refueling) that we care about as the
        # starting point.
        if remaining_gallons < city_and_gas.gas:
            city_and_gas = CityAndGas(i + 1, remaining_gallons)

    return city_and_gas.city


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure("Out of gas on city {}".format(i))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "refueling_schedule.py", "refueling_schedule.tsv", find_ample_city_wrapper
        )
    )
