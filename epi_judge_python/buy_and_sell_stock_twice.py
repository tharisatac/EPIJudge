from typing import List

from test_framework import generic_test

""" 5.7 Buy and sell stock twice. """


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    """Buy and sell a stock twice."""

    # 1) The best solutiion to this is to take advantage of the solution in
    # '5.6 buy_and_sell_stock.py'.

    # First buy and sell profits. This is O(n)
    min_price = float("inf")
    max_profit = 0
    first_buy_sell_profits = [0.0] * len(prices)
    for i in range(len(prices)):
        min_price = min(prices[i], min_price)
        profit = prices[i] - min_price
        max_profit = max(profit, max_profit)
        first_buy_sell_profits[i] = max_profit

    # Second buy and sell profits. i.e. the max profit from Day i onwards. This
    # is O(n)
    max_price_so_far = float("-inf")
    max_total_profit = 0
    for j, price in reversed(list(enumerate(prices))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit, max_price_so_far - price + first_buy_sell_profits[j]
        )

    return max_total_profit


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock_twice.py",
            "buy_and_sell_stock_twice.tsv",
            buy_and_sell_stock_twice,
        )
    )
