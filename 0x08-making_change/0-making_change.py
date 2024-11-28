#!/usr/bin/python3
"""
Determine the minimum number of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.

    Args:
        coins (list): List of coin denominations.
        total (int): Target amount.

    Returns:
        int: Minimum number of coins needed to meet total,
        or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Create an array for the minimum coins needed for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total 0

    # Update dp array for each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
