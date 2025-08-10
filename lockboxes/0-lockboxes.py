#!/usr/bin/python3
"""This is for checkink if or not we are able to unlock the boxses"""


def canUnlockAll(boxes):
    """Function for checking boxes"""
    unlocked = {0}
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

    return len(unlocked) == len(boxes)
