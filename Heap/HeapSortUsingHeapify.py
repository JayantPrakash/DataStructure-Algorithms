def heapify(A,n):
    # first non element is n/2 - 1, if n is total no of elements
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

def delete_heap(A,n):
    i = 0
    j = 1
    val = A[0]
    #swap first and last element
    A[i],A[n] = A[n],A[i]
    # check if it is less than n-1 as we have decreased size of heap by 1 
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


def heapSort(A):

    A = heapify(A,len(A)-1)
    print("after heapify::", A)
    # range is from len-1 to 1
    for i in range(len(A)-1,-1,-1):
        delete_heap(A,i)
    return A    

A = [40,45,30,35,10,25,5]

print(heapSort(A))

