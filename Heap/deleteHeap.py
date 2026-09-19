# Key idea: Track heap ordering and which element is kept at the root.
# Compute or update the delete result for the supplied input.
def delete(A, n):
    i = 0
    A[n], A[0] = A[0], A[n]
    #A[0] = A[n]
    j = 1

    # Keep processing while `j <= n - 1` remains true.
    while j <= n - 1:
        # Choose this path when `j < n - 1 and A[j] < A[j + 1]` is true.
        if j < n-1 and A[j] < A[j + 1]:
            j = j + 1

        # Choose this path when `A[j] > A[i]` is true.
        if A[j] > A[i]:
            A[i], A[j] = A[j], A[i]
            i = j
            j = j * 2 + 1
        else:
            break
    return A


array = [40, 35, 30, 15, 10, 25, 5]
array = [40, 30, 15, 20, 0, 14, 5, 8]

# print(delete(array,len(array)-1))

def deleteAll(array):
    # Process each value from `range(len(array) - 1, 0, -1)`.
    for i in range(len(array) - 1, 0, -1):
        print(i)
        A = delete(array, i)
        print(A)


deleteAll(array)
