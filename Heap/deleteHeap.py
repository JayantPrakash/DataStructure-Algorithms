# Move the maximum to index n, then repair the active max-heap at indices 0 through n-1.
# This rearranges the array rather than removing an element from the Python list.
def delete(A, n):
    i = 0
    A[n], A[0] = A[0], A[n]
    #A[0] = A[n]
    j = 1

    while j <= n - 1:
        # Select the larger child; promoting the smaller child could leave the parent below its sibling.
        if j < n-1 and A[j] < A[j + 1]:
            j = j + 1

        # Move the displaced root downward until it dominates both children, at most O(log n) levels.
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

# Shrink the heap's active boundary after each extraction; maxima accumulate in a sorted suffix.
def deleteAll(array):
    for i in range(len(array) - 1, 0, -1):
        print(i)
        A = delete(array, i)
        print(A)


deleteAll(array)
