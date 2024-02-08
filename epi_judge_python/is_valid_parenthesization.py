from test_framework import generic_test

""" 8.3 """


def is_well_formed(s: str) -> bool:
    """Checks if a string is well-formed."""
    # This is best done using a stack!

    left_chars = []
    lookup_table = {"[": "]", "{": "}", "(": ")"}
    for c in s:
        if c in lookup_table:
            # Left char. So store it.
            left_chars.append(c)
        else:
            # Check right char and match it.
            if not left_chars or lookup_table[left_chars.pop()] != c:
                return False
    return not left_chars


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_parenthesization.py",
            "is_valid_parenthesization.tsv",
            is_well_formed,
        )
    )
