# Key idea: Follow pivot placement and the recursive partitions on either side.
import random


# Compute or update the q sort result for the supplied input.
def qSort(A, start, end):
    # Choose this path when `start >= end` is true.
    if start >= end:
        return

    rand_index = random.randint(start,end)

    A[start],A[rand_index] = A[rand_index],A[start]

    pivot = A[start]
    smaller = start
    bigger = start

    # Process each value from `range(start + 1, end + 1)`.
    for bigger in range(start+1,end+1):
        # Choose this path when `A[bigger] <= pivot` is true.
        if A[bigger] <= pivot:
            smaller += 1
            A[smaller], A[bigger] = A[bigger], A[smaller]

        A[smaller], A[start] = A[start], A[smaller]

    qSort(A,start, smaller-1)
    qSort(A, smaller+1, end)

# Compute or update the quick sort result for the supplied input.
def quickSort(A):
    qSort(A,0,len(A)-1)
    return A


array = [4, 2, 8, 7, 1, 3, 5, 6]
print(quickSort(array))
