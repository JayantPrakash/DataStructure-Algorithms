import numpy as np


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = int(np.floor((low + high) / 2))
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        # we have to put mid-1 otherwise it is going to infinite loop
        else:
            return binary_search(data, target, mid + 1, high)


print(binary_search([2, 4, 6, 8, 9, 10, 13, 15], 7, 0, 7))
