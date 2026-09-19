# Intended bottom-up max-heap construction: repair each internal node by sifting downward.
# This implementation reads A[j+1] without checking that the right child is inside the active heap.
def heapify(A,n):
    for i in range(int(n/2) -1, -1, -1):
        j = 2*i + 1    
        while (j<n):
            if A[j] < A[j+1]:
                j += 1
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
                i = j    
                j = 2*j + 1
            else:
                break     
    return A

# Move the root maximum to boundary n, then attempt to repair the remaining prefix.
def delete_heap(A,n):
    i = 0
    j = 1
    val = A[0]
    #swap first and last element
    A[i],A[n] = A[n],A[i]
    # This bound can skip a final lone left child; a correct sift-down must handle that child too.
    while (j<n-1):
        # find which child is greater
        if A[j] < A[j+1]:
            j += 1
        # whichever child is greater is compared with current elem
        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]
            i = j    
            j = 2*j + 1
        # It is at right place
        else:
            break     
    return val


# The intended algorithm builds a heap once, then shrinks it after each maximum extraction.
def heapSort(A):

    # This passes the last index, while heapify's bounds resemble a count; boundary conventions need care.
    # The existing off-by-one behavior is retained here.
    A = heapify(A,len(A)-1)
    print("after heapify::", A)
    # range is from len-1 to 1
    for i in range(len(A)-1,-1,-1):
        delete_heap(A,i)
    return A    

A = [40,45,30,35,10,25,5]

print(heapSort(A))

