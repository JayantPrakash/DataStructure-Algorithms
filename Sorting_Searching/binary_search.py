# Key idea: Track the search interval and the condition that discards half of it.
# Compute or update the binary search result for the supplied input.
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    # Keep processing while `low <= high` remains true.
    while low <= high:
        mid = low + (high - low) // 2

        # Choose this path when `arr[mid] < x` is true.
        if arr[mid] < x:
            low = mid + 1
        # Choose this path when `arr[mid] > x` is true.
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)

# Choose this path when `result != -1` is true.
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")