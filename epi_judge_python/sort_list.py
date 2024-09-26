from typing import Optional

from list_node import ListNode
from test_framework import generic_test

""" 13.11 """


def _merge_two_sorted_lists(L1: ListNode, L2: ListNode) -> ListNode:
    """Merge two sorted lists."""

    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next

        tail = tail.next

    # Carry on...
    tail.next = L1 or L2
    return dummy_head.next


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    """We use merge-sort here!"""

    if L is None or L.next is None:
        return L

    # Split the list in half using a fast and a slower pointer
    pre_slow, slow, fast = None, L, L

    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next

    if pre_slow:
        pre_slow.next = None  # Split the list.

    return _merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_list.py", "sort_list.tsv", stable_sort_list
        )
    )
