# Sift down at index i within A[:n], assuming the child subtrees are already max-heaps.
# One call repairs one subtree, not an arbitrary whole array; O(log n) time and recursion space.
def heapify(A,n,i):
    largest = i

    l = 2*i + 1
    r = 2*i + 2

    # Choose the largest of parent and existing children; these while checks each run at most once.
    while l < n and A[largest] < A[l]:
        largest = l

    while r < n and A[largest] < A[r]:
        largest = r

    # Promote the largest child and recursively repair the displaced value's new subtree.
    if largest != i:
        A[largest],A[i] = A[i],A[largest]
        heapify(A,n,largest)

    return A

# The example's child subtrees are not both heaps, so a root-only repair need not produce a valid heap.
array = [15,5,20,1,17,10,30]

print(heapify(array,len(array), 0))
