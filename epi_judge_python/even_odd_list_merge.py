from typing import Optional

from list_node import ListNode
from test_framework import generic_test

""" 7.10 """


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    """Merge even and odd lists."""

    if L is None:
        return L

    dummy_even_head = ListNode(0, L)
    dummy_odd_head = ListNode(0, L)
    tails = [dummy_even_head, dummy_odd_head]
    step = 0

    while L:
        tails[step].next = L
        L = L.next
        tails[step] = tails[step].next

        step ^= 1

    tails[1].next = None
    tails[0].next = dummy_odd_head.next

    return dummy_even_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "even_odd_list_merge.py", "even_odd_list_merge.tsv", even_odd_merge
        )
    )
