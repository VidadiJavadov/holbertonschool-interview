#!/usr/bin/python3
"""This is for checkink if or not we are able to unlock the boxses"""


def canUnlockAll(boxes):
    """This function is for determine if the boxes can be opened"""
    setb = set([])
    for i in range(len(boxes)):
        for j in boxes[i]:
            if j != i and j != 0:
                setb.add(j)

    set2 = set([])
    for j in range(1, len(boxes)):
        set2.add(j)

    if(setb == set2):
        return True
    return False
