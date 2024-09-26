from typing import List

from test_framework import generic_test

""" 5.9 The Sieve of Eratosthenes """


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    """
    Sieve primes up to the passed-in number. This is done using a boolean
    array.
    """
    if n < 2:
        return []

    # 1) Method 1. Sieving with no optimization.
    # primes = [2]

    # # Set up a boolean array. Initially everything is True except for 0,1 which
    # # are guaranteed primes.
    # # It's (n-1) because 0 is naturally not included in any length.
    # is_prime = [False, False] + [True] * (n - 1)

    # # As an optimization, even numbers can be pre-emptively ignored.
    # for i in range(3, len(is_prime)):
    #     if i % 2 == 0:
    #         is_prime[i] = False

    # # n+1 to include n (remember it's exclusive.)
    # for i in range(3, n + 1):
    #     if is_prime[i]:
    #         primes.append(i)
    #         # Sieve its multiples
    #         for j in range(i * 2, n + 1, i):
    #             is_prime[j] = False

    # 2) Sieving with optimization.

    primes = [2]
    size = (n - 3) // 2 + 1  # We know that the first 3 numbers are 0,1,2

    is_prime = [True] * size
    # is_prime now checks for 2i+3 (i.e. 3, 5, 7, 9 and so on). This reduces
    # the space that is required.
    for i in range(size):
        if is_prime[i]:
            p = 2 * i + 3
            primes.append(p)

            # Sieve out its multiples from p^2 because kp where k < p would
            # already have been sieved out.

            # 2 * i**2 + 6 * i + 3 is used as its a simplified version of p^2...
            # I am not entirely sure how.
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False

    return primes


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "prime_sieve.py", "prime_sieve.tsv", generate_primes
        )
    )
