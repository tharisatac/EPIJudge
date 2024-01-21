from test_framework import generic_test

""" 6.10 """


def snake_string(s: str) -> str:
    """Use periodicity to write a sinusodial string."""

    result = []

    # Output the first row.
    for i in range(1, len(s), 4):
        result.append(s[i])

    # The second row!
    for i in range(0, len(s), 2):
        result.append(s[i])

    # The third row.
    for i in range(3, len(s), 4):
        result.append(s[i])

    return "".join(result)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "snake_string.py", "snake_string.tsv", snake_string
        )
    )
