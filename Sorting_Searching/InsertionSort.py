# Grow a sorted prefix by shifting larger values right; stable, in-place insertion sort.
# O(n^2) worst-case time and O(1) auxiliary space.
def insertion_sort(arr):
    # Already-sorted empty/singleton inputs return None in this version, unlike the final list return.
    if len(arr) <= 1:
        return

    for i in range(1,len(arr)):
        # Preserve the candidate while its original slot may be overwritten by shifted values.
        ith = arr[i]
        j = i - 1
        # The bounds check follows the lookup here; when j becomes -1, Python reads the last element before stopping.
        while arr[j] > ith and j >= 0:
            # Place the saved candidate immediately after the last smaller-or-equal prefix value.
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = ith
    return arr

print(insertion_sort([4,1,9,3,2]))
