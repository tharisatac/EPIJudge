from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

""" 9.10 """


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    """
    Inorder traversal of a binary tree with no recursion

    Inorder traversal consists of:
    - Traversing the left subtree
    - Returning to the root
    - Traverse the right subtree.
    """
    prev = None
    result = []

    while tree:
        if prev is tree.parent:
            # We just came down from the parent
            if tree.left:
                # Keep going left, all the way down!
                next = tree.left
            else:
                # We've hit a right child.
                result.append(tree.data)
                # Either go right or go back up to its parent if it's empty.
                next = tree.right or tree.parent

        elif prev is tree.left:
            # We just came up to the parent from a left child.
            result.append(tree.data)
            # Done with left, go to the right subtree or its parent.
            next = tree.right or tree.parent

        elif prev is tree.right:
            # We just came up from the right child.
            next = tree.parent

        # Previous is whatever the tree is pointing to.
        prev = tree
        # The tree is wherever we are going next!
        tree = next

    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_with_parent_inorder.py",
            "tree_with_parent_inorder.tsv",
            inorder_traversal,
        )
    )
