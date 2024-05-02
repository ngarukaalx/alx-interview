#!/usr/bin/python3
"""This module contains function makeChange"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    """
    # If total is 0 or less, return 0
    if total <= 0:
        return 0
    # sort coins in ascendind order
    sorted_coins = sorted(coins)
    # list to store coins to meet solution
    possible_coins = []
    n = len(sorted_coins)
    i = n - 1

    # iterate over all coins from the max
    while(i >= 0):
        # find the fewest coins
        while(total >= sorted_coins[i]):
            total -= sorted_coins[i]
            possible_coins.append(sorted_coins[i])
        i -= 1
    if total == 0:
        return len(possible_coins)
    return -1
