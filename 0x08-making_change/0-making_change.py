#!/usr/bin/python3
"""determines the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """
    coins - a list of coins
    total - the total to be met
    Return: fewest number of coins needed to meet total
            0 if total is 0
            -1 if total can't be met
    """
    if total < 1:
        return 0

    coins.sort()
    n = len(coins)
    i = n - 1
    count = 0

    while (i >= 0):
        while (total >= coins[i]):
            total -= coins[i]
            count += 1

        i -= 1

    if total == 0:
        return count
    else:
        return -1
