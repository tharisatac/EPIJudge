from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test

""" 14.5 """


def rebuild_bst_from_preorder(preorder_sequence: List[int]) -> Optional[BstNode]:
    """Build a BST from preorder"""
    # Preorder is root, then left subtree then right subtree.
    # Let's construct the left subtree as we go. This makes it an O(n) operation

    def _helper(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            # If we've come this far, return None
            return None

        # Otherwise, go down the subtree
        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            # This makes sure that we exit the sequence properly for the left
            # and the right subtree
            return None

        root_idx[0] += 1

        left_subtree = _helper(lower_bound, root)
        right_subtree = _helper(root, upper_bound)

        return BstNode(root, left_subtree, right_subtree)

    # Use a list as it's mutable
    root_idx = [0]

    return _helper(float("-inf"), float("inf"))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "bst_from_preorder.py", "bst_from_preorder.tsv", rebuild_bst_from_preorder
        )
    )
