#!/user/bin/python3
"""A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False."""

    keys = set()

    # print(boxes)
    print(f"range is {len(boxes)}")
    for index in range(len(boxes)):
    # print(f"range is {len(boxes[index])}")
        for inner_index in range(len(boxes[index])):
            if (boxes[index][inner_index] >= len(boxes)):
                continue
            elif (boxes[index][inner_index] == 0):
                continue
            else:
                keys.add(boxes[index][inner_index])

    print(f"Keys are {keys}")
    if (len(keys) == len(boxes) - 1):
        return True
    else:
        return False
