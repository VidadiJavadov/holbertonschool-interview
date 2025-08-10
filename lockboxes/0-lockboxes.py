#!/usr/bin/python3
"""This is for checkink if or not we are able to unlock the boxses"""


def canUnlockAll(boxes):
    """This function checks the aviability of unlocking the boxes"""
    setb = set([])
    for i in range(len(boxes)):
        for j in boxes[i]:
            if j != i:
                setb.add(j)

    set2 = set([])
    for j in range(len(boxes)):
        set2.add(j)

    if(setb == set2):
        return True
    return False
