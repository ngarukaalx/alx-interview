#!/usr/bin/python3
"""This module contains func minOperations
and primeGenerator()
"""


def primeGenerator():
    """generates prime numbers"""
    yield 2
    primeNumbers = [2]
    num = 3
    while True:
        # if num is not divisible by all numbers in the list
        # then its a prime number
        if all(num % prime != 0 for prime in primeNumbers):
            primeNumbers.append(num)
            yield num
        num += 2


def minOperations(n):
    """In a text file, there is a single character H. Your text
    editor can execute only two operations in this file: Copy All
    and Paste. Given a number n, write a method that calculates the
    fewest number of operations needed to result in exactly n H
    characters in the file.
    If n is impossible to achieve, return 0
    Returns an integer
    """
    if isinstance(n, int) and n > 1:
        primes = primeGenerator()
        num = n
        min_operations = 0
        while True:
            x = next(primes)
            if x > num:
                break
            while num % x == 0:
                firstPrime = num / x
                num = firstPrime
                min_operations += x
        return min_operations
    else:
        return 0
