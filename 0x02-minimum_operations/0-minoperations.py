#!/usr/bin/python3
"""a method that calculates the fewest number of operations needed to
 result in exactly n H characters in the file.
"""


def minOperations(n):
    """Returns the number of operations if possible
    Returns 0 if not possible.
    """

    if (n <= 1):
        return 0

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    sum = 0
    for num in factors:
        sum += num

    return sum
