from test_framework import generic_test
from test_framework.test_failure import TestFailure

""" 8.7 """


class Queue:
    QUEUE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        self._entries = [0] * capacity
        self._head = 0
        self._tail = 0
        self._num_entries = 0

    def enqueue(self, x: int) -> None:
        # Check for resizing
        if self._num_entries == len(self._entries):
            # Resize! First, unwrap the circular queue.
            self._entries = self._entries[self._head :] + self._entries[: self._head]
            self._head = 0
            self._tail = self._num_entries
            self._entries += [0] * (
                len(self._entries) * Queue.QUEUE_FACTOR - len(self._entries)
            )

        # The tail is always pointing to the next location
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_entries += 1

    def dequeue(self) -> int:
        self._num_entries -= 1
        result = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return result

    def size(self) -> int:
        return self._num_entries


def queue_tester(ops):
    q = Queue(1)

    for op, arg in ops:
        if op == "Queue":
            q = Queue(arg)
        elif op == "enqueue":
            q.enqueue(arg)
        elif op == "dequeue":
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result)
                )
        elif op == "size":
            result = q.size()
            if result != arg:
                raise TestFailure("Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "circular_queue.py", "circular_queue.tsv", queue_tester
        )
    )
