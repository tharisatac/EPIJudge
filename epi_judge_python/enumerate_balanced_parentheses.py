from typing import List

from test_framework import generic_test, test_utils

""" 15.7 """


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    """Generate balanced parentheses"""

    def _backtrack(num_left_needed, num_right_needed, valid_prefix, result=[]):

        if num_left_needed > 0:
            # We can add a left parentheses
            _backtrack(num_left_needed - 1, num_right_needed, valid_prefix + "(")

        if num_left_needed < num_right_needed:
            # Add a right parentheses
            _backtrack(num_left_needed, num_right_needed - 1, valid_prefix + ")")

        if not num_right_needed:
            # We don't need any more right
            result.append(valid_prefix)
        return result

    return _backtrack(num_pairs, num_pairs, valid_prefix="")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "enumerate_balanced_parentheses.py",
            "enumerate_balanced_parentheses.tsv",
            generate_balanced_parentheses,
            test_utils.unordered_compare,
        )
    )
