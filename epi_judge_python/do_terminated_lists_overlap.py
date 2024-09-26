import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

""" 7.4 """


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    """Do linked lists overlap?"""

    def length(l: ListNode) -> int:
        """Finds the length of the linked list."""
        length = 0
        while l:
            length += 1
            l = l.next

        return length

    l0_len = length(l0)
    l1_len = length(l1)

    if l1_len > l0_len:
        # Make l0 the longer one
        l1, l0 = l0, l1

    for _ in range(abs(l0_len - l1_len)):
        l0 = l0.next

    while l0 and l1 and l0 is not l1:
        l0 = l0.next
        l1 = l1.next

    # This will be None if there is no overlap
    return l1


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure("Invalid result")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "do_terminated_lists_overlap.py",
            "do_terminated_lists_overlap.tsv",
            overlapping_no_cycle_lists_wrapper,
        )
    )
