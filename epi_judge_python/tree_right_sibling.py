import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

""" Create a tree with a next_level attribute """


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.


def construct_right_sibling(tree: BinaryTreeNode) -> None:
    """Construct the right sibling."""

    def _populate_next(start_node):
        while start_node and start_node.left:
            # Populate the next field.
            start_node.left.next = start_node.right

            # Populate the next field of the right node.
            if start_node.next:
                start_node.right.next = start_node.next.left

            # Keep goin!
            start_node = start_node.next

    while tree:
        _populate_next(tree)
        tree = tree.left


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)] for level in traverse_left(cloned)]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_right_sibling.py",
            "tree_right_sibling.tsv",
            construct_right_sibling_wrapper,
        )
    )
