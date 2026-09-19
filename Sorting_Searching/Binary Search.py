import numpy as np


# Search an inclusive interval in sorted input; each recursive call discards half its candidates.
# O(log n) time and O(log n) call-stack space; this returns a boolean.
def binary_search(data, target, low, high):
    # The interval is empty, so all candidate positions have been ruled out.
    if low > high:
        return False
    else:
        mid = int(np.floor((low + high) / 2))
        if target == data[mid]:
            return True
        # Sorted order rules out mid and everything to its right when target is smaller.
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            # Exclude the already-tested midpoint so even a one-element interval makes progress.
            return binary_search(data, target, mid + 1, high)


print(binary_search([2, 4, 6, 8, 9, 10, 13, 15], 7, 0, 7))
