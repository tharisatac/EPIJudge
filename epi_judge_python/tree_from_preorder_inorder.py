from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

""" 9.11 """


def binary_tree_from_preorder_inorder(
    preorder: List[int], inorder: List[int]
) -> BinaryTreeNode:
    """
    Given an in order traversal sequence and a preorder traversal
    sequence of a binary tree, reconstruct the tree.
    """
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def _create_tree(preorder_start, preorder_end, inorder_start, inorder_end):
        """Create a tree helper function!"""

        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            # We've reached the end.
            return None

        # Get the idx at which the root node is in the in-order sequence.
        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start

        return BinaryTreeNode(
            preorder[preorder_start],
            # Create the left subtree, recursively
            _create_tree(
                # Append 1 to the preorder start order (This is the root of the
                # next in-order traversal)
                preorder_start + 1,
                # The left_subtree_size is the difference between where its root
                # is and where it's started from. In this case, it is 4, thus,
                # the inorder end = 5, is correct as it ensures everything is
                # encapsulated.
                preorder_start + 1 + left_subtree_size,
                # The inorder start for the left subtree is always the same as
                # the parent's.
                inorder_start,
                # The inorder end, will of course, be the parent's index for the
                # left subtree.
                root_inorder_idx,
            ),
            # Create the right subtree
            _create_tree(
                # The preorder start is thus where the preorder of the left
                # subtree ends.
                preorder_start + 1 + left_subtree_size,
                # The preorder end for a right subtree is always at the end.
                preorder_end,
                # The inorder start of the right subtree is one more than the
                # root index
                root_inorder_idx + 1,
                # The inorder end is just the inorder end.
                inorder_end,
            ),
        )

    return _create_tree(
        preorder_start=0,
        preorder_end=len(preorder),
        inorder_start=0,
        inorder_end=len(inorder),
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_from_preorder_inorder.py",
            "tree_from_preorder_inorder.tsv",
            binary_tree_from_preorder_inorder,
        )
    )
