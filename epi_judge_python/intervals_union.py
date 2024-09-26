import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple("Endpoint", ("is_closed", "val"))

Interval = collections.namedtuple("Interval", ("left", "right"))

""" 13.8 """


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    """Find the union of intervals"""

    if not intervals:
        return []

    # First sort them
    intervals.sort(
        key=lambda v: (v.left.val, not v.left.is_closed)
    )  # Remember that False comes before True (and we want is_closed first)

    result = [intervals[0]]

    for i in intervals:
        # Is it in the current interval?
        if (
            # If the left value is less than the right value of the current
            # interval then it must be in the interval.
            i.left.val
            < result[-1].right.val
        ) or (
            # If the left value is equal to the right value of the current
            # interval and one of them is closed (and therefore the interval)
            # is continuous.
            i.left.val == result[-1].right.val
            and (i.left.is_closed or result[-1].right.is_closed)
        ):
            # Now, the current interval is only worth updating if the right of
            # the new interval > the right of the current interval or they are
            # equal but the new interval is closed (and therefore technically
            # greater)
            if i.right.val > result[-1].right.val or (
                i.right.val == result[-1].right.val and i.right.is_closed
            ):
                # Merge the union interval.
                result[-1] = Interval(result[-1].left, i.right)

        else:
            # New interval.
            result.append(i)

    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [
        (i.left.val, i.left.is_closed, i.right.val, i.right.is_closed) for i in result
    ]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intervals_union.py", "intervals_union.tsv", union_of_intervals_wrapper
        )
    )
