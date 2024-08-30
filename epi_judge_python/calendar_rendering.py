import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple("Event", ("start", "finish"))

""" 13.6 """


def find_max_simultaneous_events(A: List[Event]) -> int:
    """Find the maximum number of simultaneous events using Endpoints."""

    Endpoint = collections.namedtuple("Endpoint", ("time", "is_start"))

    E = [
        p
        for event in A
        for p in (Endpoint(event.start, True), Endpoint(event.finish, False))
    ]

    # Let's sort
    E.sort(key=lambda v: (v.time, not v.is_start))

    # Let's get to work.
    max_result = 0
    curr_events = 0
    for e in E:
        if e.is_start:
            curr_events += 1
        else:
            curr_events -= 1

        max_result = max(curr_events, max_result)

    return max_result


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events, events))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "calendar_rendering.py",
            "calendar_rendering.tsv",
            find_max_simultaneous_events_wrapper,
        )
    )
