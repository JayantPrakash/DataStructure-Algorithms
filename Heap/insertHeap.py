# Key idea: Track heap ordering and which element is kept at the root.

#insert one element in heap
def insert(A, n):
    i = n
    temp = A[n]

    # Keep processing while `i > 0 and temp > A[int(i / 2)]` remains true.
    while i > 0 and temp > A[int(i / 2)]:
        A[i] = A[int(i / 2)]
        i = int(i / 2)

    A[i] = temp
    return A
array = [40, 35, 15, 30, 10, 12, 6, 5, 20, 50]

print(insert(array, n=9))

#T(n) = O(logn)
#S(n) = O(n)