#!/usr/bin/python3
"""This module contains function canUnlockAll()
"""


def canUnlockAll(boxes):
    """function to determine if all boxes can be opened
       args: boxes - list of lists
    """

    if not boxes:
        return False

    n = len(boxes)
    checked = [False] * n
    stack = [0]

    while stack:
        box = stack.pop()
        checked[box] = True

        for key in boxes[box]:
            if 0 <= key < n and not checked[key]:
                stack.append(key)
    return all(checked)
