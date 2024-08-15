#!/user/bin/python3
"""A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False."""
    keys = set()

    for index in range(len(boxes)):

