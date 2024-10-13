#!/usr/bin/python3


def canUnlockAll(boxes):
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
