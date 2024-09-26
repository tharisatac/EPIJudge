from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

""" 9.2 """


def is_symmetric(tree: BinaryTreeNode) -> bool:
    """Checks if a tree is symmetric."""

    def _check_symmetric(tree1: BinaryTreeNode, tree2: BinaryTreeNode) -> bool:
        """Checks if the trees are symmetric, recursively."""
        if not tree1 and not tree2:
            # The check is finished.
            return True
        elif tree1 and tree2:
            return (
                tree1.data == tree2.data
                and _check_symmetric(tree1.left, tree2.right)
                and _check_symmetric(tree1.right, tree2.left)
            )
        return False

    return _check_symmetric(tree.left, tree.right) if tree else True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
