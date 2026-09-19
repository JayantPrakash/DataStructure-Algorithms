# Repair a max-heap subtree by moving its root down, assuming the child subtrees are heaps.
def heapify(A,n,i):
    largest = i

    l = 2*i + 1
    r = 2*i + 2

    # Find the largest existing child or keep i; each of these while conditions runs at most once.
    while l < n and A[largest] < A[l]:
        largest = l

    while r < n and A[largest] < A[r]:
        largest = r

    # After a swap, only the child's subtree can still violate heap order.
    if largest != i:
        A[largest],A[i] = A[i],A[largest]
        heapify(A,n,largest)

    return A

# Build a max-heap, then repeatedly place its maximum at the end of the unsorted prefix.
# O(n log n) time and O(log n) recursion space; empty input leaves A undefined in this version.
def heapSort(array):
    n = len(array)
    if n == 1:
        return array
    # Visit internal nodes from bottom to top; the children are already heaps when their parent is repaired.
    # This construction phase is O(n), since most nodes are near the leaves.
    for i in range(int(n/2) - 1,-1,-1):
        A = heapify(array,len(array), i)
    #print(A)
    # Freeze the maximum at i, and pass i as the smaller exclusive heap boundary.
    for i in range(n-1,-1,-1):
        A[i],A[0] = A[0], A[i]
        A = heapify(array,i,0)
    #print(A)
    return A


array = [15,5,20,1,17,10,30]
array = [8,5,2,9,5,6,3]

print(heapSort(array))

