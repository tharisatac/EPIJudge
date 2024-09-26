from list_node import ListNode
from test_framework import generic_test

""" 7.11 - is list palindromic? """


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # First write the reverse_list function
    def reverse_list(_node: ListNode) -> ListNode:
        """Reverse a linked-list."""
        dummy_head = ListNode(0)
        while _node:
            # dummy_head.next, _node.next, _node = _node, dummy_head.next, _node.next
            temp = _node.next

            _node.next = dummy_head.next
            dummy_head.next = _node

            _node = temp

        return dummy_head.next

    # Find the middle of the list
    slow = fast = L
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Compare the two linked lists
    first_half_iter, second_half_iter = L, reverse_list(slow)
    while second_half_iter and first_half_iter:
        if first_half_iter.data != second_half_iter.data:
            return False
        second_half_iter = second_half_iter.next
        first_half_iter = first_half_iter.next

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_list_palindromic.py",
            "is_list_palindromic.tsv",
            is_linked_list_a_palindrome,
        )
    )
