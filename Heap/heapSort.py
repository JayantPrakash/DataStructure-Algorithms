# insert one element in heap
# Sift up by shifting ancestors down and saving the new value until its destination is found.
# This uses i // 2 as parent; standard zero-based heaps require (i - 1) // 2.
def insert(A, n):
    i = n
    temp = A[n]

    while i > 0 and temp > A[int(i / 2)]:
        A[i] = A[int(i / 2)]
        i = int(i / 2)

    A[i] = temp
    return A


# Swap the root with the active last position, then sift the replacement toward the larger child.
def delete(A, n):
    i = 0
    A[n], A[0] = A[0], A[n]

    j = 1

    while j <= n - 1:
        if A[j] < A[j + 1] and j < n - 1:
            j = j + 1

        if A[j] > A[i]:
            A[i], A[j] = A[j], A[i]
            i = j
            # Deletion uses zero-based children, unlike the parent convention in insert.
            # The mismatch means this implementation is not a reliable general heapsort.
            j = j * 2 + 1
        else:
            break
    return A


array = [0, 14, 15, 5, 20, 30, 8, 40]


# The intended invariant is an unsorted heap prefix followed by a sorted suffix of extracted maxima.
def heapSort(array):
    for i in range(1, len(array)):
        insert(array, i)
    print(array)

    # Each extraction decreases the active heap boundary; output is printed after every step.
    for i in range(len(array) - 1, 0, -1):
        array = delete(array, i)
        print(i)
        print(array)


heapSort(array)
