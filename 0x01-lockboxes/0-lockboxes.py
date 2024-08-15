#!/usr/bin/python3
"""A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False.
    """
    keys = set()

    for index in range(len(boxes)):
        for inner_index in range(len(boxes[index])):
            if (boxes[index][inner_index] >= len(boxes)):
                continue
            elif (boxes[index][inner_index] == 0):
                continue
            elif (boxes[index][inner_index] == index):
                continue
            else:
                keys.add(boxes[index][inner_index])

    if (len(keys) == len(boxes) - 1):
        return True
    else:
        return False
