from typing import List

from test_framework import generic_test

""" 5.6 Buy and sell stock once."""


def buy_and_sell_stock_once(prices: List[float]) -> float:
    """Buy and sell stock once."""

    # 1) A brute force algorithm would be to calculate the maximum difference
    # between any two sets of prices j and i, where j>i. This is clearly an
    # O(n^2) algorithm and is frigtheningly slow.
    # Space complexity is a constant O(1).
    # max_profit = 0
    # for i in range(len(prices)):
    # for j in range(i, len(prices)):
    # if prices[j] - prices[i] > max_profit:
    # max_profit = prices[j] - prices[i]

    # 2) A better algorithm, is to appreciate the fact that the max profit
    # that can be made on any one day is the difference between its value and
    # the minimum price seen so far.
    # O(n) time complexity. O(1) space complexity.
    min_price = float("inf")
    max_profit = 0
    for i in range(len(prices)):
        min_price = min(prices[i], min_price)
        profit = prices[i] - min_price
        max_profit = max(profit, max_profit)

    return max_profit


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
