
#in mean heap only temp < A[int(i / 2)] condition changes.
# insert one element in heap
def insert(A, n):
    i = n
    temp = A[n]

    while i > 0 and temp < A[int(i / 2)]:
        A[i] = A[int(i / 2)]
        i = int(i / 2)

    A[i] = temp
    return A


def createHeap(A):
    for i in range(1, len(A)):
        A = insert(A, i)

    return A


array = [10, 20, 30, 25, 5, 40, 35]

print(createHeap(array))
