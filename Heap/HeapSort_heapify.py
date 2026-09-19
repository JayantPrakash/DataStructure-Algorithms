# Key idea: Track heap ordering and which element is kept at the root.
# Compute or update the heapify result for the supplied input.
def heapify(A,n,i):
    largest = i

    l = 2*i + 1
    r = 2*i + 2

    # Keep processing while `l < n and A[largest] < A[l]` remains true.
    while l < n and A[largest] < A[l]:
        largest = l

    # Keep processing while `r < n and A[largest] < A[r]` remains true.
    while r < n and A[largest] < A[r]:
        largest = r

    # Choose this path when `largest != i` is true.
    if largest != i:
        A[largest],A[i] = A[i],A[largest]
        heapify(A,n,largest)

    return A

# Compute or update the heap sort result for the supplied input.
def heapSort(array):
    n = len(array)
    # Choose this path when `n == 1` is true.
    if n == 1:
        return array
    # Process each value from `range(int(n / 2) - 1, -1, -1)`.
    for i in range(int(n/2) - 1,-1,-1):
        A = heapify(array,len(array), i)
    #print(A)
    for i in range(n-1,-1,-1):
        A[i],A[0] = A[0], A[i]
        A = heapify(array,i,0)
    #print(A)
    return A


array = [15,5,20,1,17,10,30]
array = [8,5,2,9,5,6,3]

print(heapSort(array))

