# Keep target's possible positions within inclusive [low, high] in an ascending array.
# Each comparison halves the interval: O(log n) time and O(1) space.
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # The midpoint and every smaller value cannot match, so the new lower bound is mid+1.
        if arr[mid] < x:
            low = mid + 1
        # The midpoint and everything to its right are too large, so the upper bound becomes mid-1.
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    # An empty candidate interval proves the target is absent.
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")