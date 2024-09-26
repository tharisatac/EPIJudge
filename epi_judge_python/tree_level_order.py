from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

""" 8.6 """


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    """Output a binary tree by depth order."""

    if not tree:
        return []

    result: List[List[int]] = []
    curr_nodes = [tree]
    while curr_nodes:
        result.append([curr.data for curr in curr_nodes])
        curr_nodes = [
            child for curr in curr_nodes for child in (curr.left, curr.right) if child
        ]
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_level_order.py", "tree_level_order.tsv", binary_tree_depth_order
        )
    )
