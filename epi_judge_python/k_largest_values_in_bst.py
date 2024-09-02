from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

""" 14.3i """


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    """Do a reverse in-order-traversal (right -> root -> left)"""

    def _helper(tree: BstNode) -> None:
        if tree and len(k_largest) < k:
            _helper(tree.right)
            if len(k_largest) < k:
                k_largest.append(tree.data)
                _helper(tree.left)

    k_largest = []
    _helper(tree)

    return k_largest


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py",
            "k_largest_values_in_bst.tsv",
            find_k_largest_in_bst,
            test_utils.unordered_compare,
        )
    )
