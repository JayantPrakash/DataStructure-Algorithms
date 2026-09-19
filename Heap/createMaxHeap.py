# insert one element in heap
# Sift up: save the inserted value, shift violating ancestors down, then fill the final hole.
# For a max-heap, a larger value moves toward the root; one insertion takes O(log n).
def insert(A, n):
    i = n
    temp = A[n]

    # This code uses i // 2 for the parent; standard zero-based heaps use (i - 1) // 2.
    # With ordinary zero-based arrays, that convention can miss the actual parent.
    while i > 0 and temp > A[int(i / 2)]:
        A[i] = A[int(i / 2)]
        i = int(i / 2)

    # Place the saved value once its chosen ancestor chain no longer violates the comparison.
    A[i] = temp
    return A


# Repeated insertion grows a heap prefix, costing O(n log n) time and O(1) auxiliary space.
# The parent-index caveat above applies to the whole construction.
def createHeap(A):
    for i in range(1, len(A)):
        A = insert(A, i)

    return A


array = [10, 20, 30, 25, 5, 40, 35]

print(createHeap(array))
