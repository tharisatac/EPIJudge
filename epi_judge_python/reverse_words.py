import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

""" 6.6  """


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    """Reverse words in a list."""

    # The best way is to reverse the entire list then re-reverse each word.
    # This is an O(n) time complexity and O(1) space. Copying into a new list
    # wastes space complexity!

    def reverse_range(s, start, end):
        """Reverses the range."""
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    # Reverse the list first.
    reverse_range(s, 0, len(s) - 1)

    # Reverse each individual word in the string
    start = 0
    while True:
        end = start
        while end < len(s) and s[end] != " ":
            end += 1

        if end == len(s):
            break
        reverse_range(s, start, end - 1)

        start = end + 1

    # Reverse the last word.
    reverse_range(s, start, end - 1)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return "".join(s_copy)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_words.py", "reverse_words.tsv", reverse_words_wrapper
        )
    )
