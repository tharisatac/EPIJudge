from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

""" 14.1 """


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    """Binary search tree."""

    QueueEntry = collections.namedtuple("QueueEntry", ("lower", "upper", "node"))

    # Use a queue!
    bfs_search = collections.deque(
        [
            QueueEntry(
                float("-inf"),
                float("inf"),
                tree,
            )
        ]
    )

    while bfs_search:
        # Popleft to get the first or the head node
        first = bfs_search.popleft()

        if first.node:
            if not first.lower <= first.node.data <= first.upper:
                return False

            bfs_search.extend(
                [
                    (QueueEntry(first.lower, first.node.data, first.node.left)),
                    (QueueEntry(first.node.data, first.upper, first.node.right)),
                ]
            )

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_a_bst.py", "is_tree_a_bst.tsv", is_binary_tree_bst
        )
    )
