# Key idea: Track the sorted prefix while each new value is inserted.
# Compute or update the insertion sort result for the supplied input.
def insertion_sort(arr):
    # Choose this path when `len(arr) <= 1` is true.
    if len(arr) <= 1:
        return

    # Process each value from `range(1, len(arr))`.
    for i in range(1,len(arr)):
        ith = arr[i]
        j = i - 1
        # Keep processing while `arr[j] > ith and j >= 0` remains true.
        while arr[j] > ith and j >= 0:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = ith
    return arr

print(insertion_sort([4,1,9,3,2]))
