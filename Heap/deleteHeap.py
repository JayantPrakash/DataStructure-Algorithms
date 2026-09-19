def delete(A, n):
    i = 0
    A[n], A[0] = A[0], A[n]
    #A[0] = A[n]
    j = 1

    while j <= n - 1:
        if j < n-1 and A[j] < A[j + 1]:
            j = j + 1

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
    for i in range(len(array) - 1, 0, -1):
        print(i)
        A = delete(array, i)
        print(A)


deleteAll(array)
