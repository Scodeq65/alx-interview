#!/usr/bin/python3
"""A method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists): Each list contains keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, else False.
    """
    n = len(boxes)
    opened_boxes = set([0])  # Start with the first box (0) unlocked
    keys = set(boxes[0])  # Keys found in the first box

    # Traverse boxes while there are keys to use
    while keys:
        key = keys.pop()  # Get a key
        """ Valid key and box not yet opened"""
        if key < n and key not in opened_boxes:
            opened_boxes.add(key)  # Mark the box as opened
            keys.update(boxes[key])  # Add the keys from this box to the set

    # If all boxes have been opened, return True
    return len(opened_boxes) == n
