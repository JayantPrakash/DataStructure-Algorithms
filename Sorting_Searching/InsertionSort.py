def insertion_sort(arr):
    if len(arr) <= 1:
        return

    for i in range(1,len(arr)):
        ith = arr[i]
        j = i - 1
        while arr[j] > ith and j >= 0:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = ith
    return arr

print(insertion_sort([4,1,9,3,2]))
