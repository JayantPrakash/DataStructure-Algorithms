# Key idea: Track the search interval and the condition that discards half of it.
import numpy as np


# Compute or update the binary search result for the supplied input.
def binary_search(data, target, low, high):
    # Choose this path when `low > high` is true.
    if low > high:
        return False
    else:
        mid = int(np.floor((low + high) / 2))
        # Choose this path when `target == data[mid]` is true.
        if target == data[mid]:
            return True
        # Choose this path when `target < data[mid]` is true.
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        # we have to put mid-1 otherwise it is going to infinite loop
        else:
            return binary_search(data, target, mid + 1, high)


print(binary_search([2, 4, 6, 8, 9, 10, 13, 15], 7, 0, 7))
