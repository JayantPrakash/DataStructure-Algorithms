import random


def qSort(A, start, end):
    if start >= end:
        return

    rand_index = random.randint(start,end)

    A[start],A[rand_index] = A[rand_index],A[start]

    pivot = A[start]
    smaller = start
    bigger = start

    for bigger in range(start+1,end+1):
        if A[bigger] <= pivot:
            smaller += 1
            A[smaller], A[bigger] = A[bigger], A[smaller]

        A[smaller], A[start] = A[start], A[smaller]

    qSort(A,start, smaller-1)
    qSort(A, smaller+1, end)

def quickSort(A):
    qSort(A,0,len(A)-1)
    return A


array = [4, 2, 8, 7, 1, 3, 5, 6]
print(quickSort(array))
