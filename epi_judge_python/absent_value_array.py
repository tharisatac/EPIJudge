from typing import Iterator
import itertools

from test_framework import generic_test
from test_framework.test_failure import TestFailure

""" 11.9 """


def find_missing_element(stream: Iterator[int]) -> int:
    """Find the missing element using a bit array"""

    # Find candidates first
    num_bucket = 1 << 16  # 2^16
    bucket = [0] * num_bucket
    stream, stream_copy = itertools.tee(stream)

    # Stream is the list of IP addresses
    for x in stream:
        upper_part_x = x >> 16
        bucket[upper_part_x] += 1

    # Look for a bucket that has less than (1 << 16) elements (or 2^16) as that
    # indicates a missing IP address.
    bucket_capacity = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(bucket) if c < bucket_capacity)

    # Finds all IP addresses in the stream whose first 16 bits are equal to
    # candidate bucket
    candidates = [0] * bucket_capacity
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            lower_part_x = ((1 << 16) - 1) & x
            candidates[lower_part_x] = 1

    # Find where candidates is 0
    for i, c in enumerate(candidates):
        if c == 0:
            return (candidate_bucket << 16) | i


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure("{} appears in stream".format(res))
    except ValueError:
        raise TestFailure("Unexpected no missing element exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "absent_value_array.py",
            "absent_value_array.tsv",
            find_missing_element_wrapper,
        )
    )
