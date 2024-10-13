#!/usr/bin/python3
"""
LockBoxes
"""


def canUnlockAll(boxes):
    """
    Write a method that determines if all the boxes can be opened.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = set(boxes[0])

    while keys:
        newKey = keys.pop()
        if newKey < n and not opened[newKey]:
            opened[newKey] = True
            keys.update(boxes[newKey])

    return all(opened)
