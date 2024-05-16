#!/usr/bin/python3
"""This module contains the prime game implementation"""


def is_prime(n):
    """fuction to check if a number is a prime num"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    """

    current_list = []
    maria = 0
    ben = 0
    maria_win = 0
    ben_win = 0

    for i in range(x):
        for j in range(1, nums[i] + 1):
            current_list.append(j)
        k = 0
        while k < len(current_list):
            prime = is_prime(current_list[k])
            if maria <= ben:
                maria += 1
                maria_turn = True
                ben_turn = False
            else:
                ben += 1
                maria_turn = False
                ben_turn = True
            if prime:
                # save current number and delete it
                temp = current_list[k]
                del current_list[k]
                num = 0
                while num < len(current_list):
                    # delete its divisibles
                    if current_list[num] % temp == 0:
                        del current_list[num]
                    num += 1
                temp = 0
                # increment maria and ben but starting with maria
                # to restart the loop
                k = 0
            else:

                k += 1
        if len(current_list) < 2:
            if ben_turn:
                maria_win += 1
            if maria_turn:
                ben_win += 1

        current_list = []
    if maria_win > ben_win:
        return "Maria"
    elif ben_win > maria_win:
        return "Ben"
    else:
        return None
