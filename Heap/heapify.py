def heapify(A,n,i):
    largest = i

    l = 2*i + 1
    r = 2*i + 2

    while l < n and A[largest] < A[l]:
        largest = l

    while r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        A[largest],A[i] = A[i],A[largest]
        heapify(A,n,largest)

    return A

array = [15,5,20,1,17,10,30]

print(heapify(array,len(array), 0))
