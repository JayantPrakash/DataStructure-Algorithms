# Key idea: Track heap ordering and which element is kept at the root.
# insert one element in heap
def insert(A, n):
    i = n
    temp = A[n]

    # Keep processing while `i > 0 and temp > A[int(i / 2)]` remains true.
    while i > 0 and temp > A[int(i / 2)]:
        A[i] = A[int(i / 2)]
        i = int(i / 2)

    A[i] = temp
    return A


# Compute or update the create heap result for the supplied input.
def createHeap(A):
    # Process each value from `range(1, len(A))`.
    for i in range(1, len(A)):
        A = insert(A, i)

    return A


array = [10, 20, 30, 25, 5, 40, 35]

print(createHeap(array))

#T(n) = O(nlogn)
#S(n) = O(n)
#here creating the max heap is inplace that means no extra array is required.