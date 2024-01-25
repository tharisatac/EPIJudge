from typing import Optional

from list_node import ListNode
from test_framework import generic_test

""" 7.2 Reverse sublist """


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    """Imagine a sublist of 11 -> 5 -> 7 -> 9 -> 2"""
    # First find the start of the node.
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next  # This gets to 11

    # Second, reverse the list
    sublist_iter = sublist_head.next  # 5
    for _ in range(finish - start):
        temp_node = sublist_iter.next  # 7
        # Make 5 point to 9
        sublist_iter.next = temp_node.next
        # Make 7 point to 5
        temp_node.next = sublist_head.next
        # Make 11 point to 7
        # 11 -> 7 -> 5 -> 9 -> 2
        sublist_head.next = temp_node

    """ 
    11 -> 7 -> 5 -> 9 -> 2
    
    # Set temp_node as 9.
    # Set 5 to point to 2
    # Set 9 to point to 7
    # Set 11 to point to 9
    
    
    """

    return dummy_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
