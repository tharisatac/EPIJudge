from test_framework import generic_test
from test_framework.test_failure import TestFailure

import collections

""" 12.3 """


class LruCache:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._isbn_table: collections.OrderedDict[int, int] = collections.OrderedDict()

    def lookup(self, isbn: int) -> int:
        try:
            price = self._isbn_table.pop(isbn)
            self._isbn_table[isbn] = price
            return price
        except KeyError:
            return -1

    def insert(self, isbn: int, price: int) -> None:
        try:
            price = self._isbn_table.pop(isbn)
        except KeyError:
            if len(self._isbn_table) == self._capacity:
                self._isbn_table.popitem(last=False)
        finally:
            self._isbn_table[isbn] = price

    def erase(self, isbn: int) -> bool:
        try:
            self._isbn_table.pop(isbn)
        except KeyError:
            return False
        return True


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != "LruCache":
        raise RuntimeError("Expected LruCache as first command")

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == "lookup":
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    "Lookup: expected " + str(cmd[2]) + ", got " + str(result)
                )
        elif cmd[0] == "insert":
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == "erase":
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    "Erase: expected " + str(cmd[2]) + ", got " + str(result)
                )
        else:
            raise RuntimeError("Unexpected command " + cmd[0])


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lru_cache.py", "lru_cache.tsv", lru_cache_tester
        )
    )
