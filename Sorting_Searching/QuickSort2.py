import random


# The intended partition keeps <= pivot values on the left and larger values on the right.
def qSort(A, start, end):
    if start >= end:
        return

    # Random pivot choice helps avoid consistently poor splits from ordered inputs.
    rand_index = random.randint(start,end)

    A[start],A[rand_index] = A[rand_index],A[start]

    pivot = A[start]
    smaller = start
    bigger = start

    for bigger in range(start+1,end+1):
        # Move qualifying values into the growing small-value region.
        if A[bigger] <= pivot:
            smaller += 1
            A[smaller], A[bigger] = A[bigger], A[smaller]

        # This pivot-placement swap is inside the scan loop; it should conceptually happen after partitioning.
        # Repeatedly moving it here breaks the partition invariant, so this version is not a reliable quicksort.
        A[smaller], A[start] = A[start], A[smaller]

    qSort(A,start, smaller-1)
    qSort(A, smaller+1, end)

# The wrapper mutates and returns A; the partition caveat above applies to the result.
def quickSort(A):
    qSort(A,0,len(A)-1)
    return A


array = [4, 2, 8, 7, 1, 3, 5, 6]
print(quickSort(array))
