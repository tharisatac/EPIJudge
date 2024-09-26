from test_framework import generic_test

""" 6.7"""


def look_and_say(n: int) -> str:
    """Fairly complicated. Recommend looking at the book."""

    def _count_number(s):
        """Count the consecutive numbers"""
        result = []
        i = 0

        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1

            result.append(str(count) + s[i])
            i += 1

        return "".join(result)

    s = "1"
    for i in range(1, n):
        s = _count_number(s)

    return s


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "look_and_say.py", "look_and_say.tsv", look_and_say
        )
    )
