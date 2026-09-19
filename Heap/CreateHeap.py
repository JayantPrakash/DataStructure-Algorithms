def insert(A, n):
    i = n
    temp = A[n]
    #[40,45] -> [40,40] -> It will go infinite loop if i>=0, so its only i > 0
    while(i > 0 and temp > A[int(i/2)]):
        A[i] = A[int(i/2)]
        i = int(i/2)

    A[i] = temp

    return A    

def create_heap(A):
    for i in range(1, len(A)):
        insert(A,i)

    return A    

nums = [5,8,14,7,19,10,6]
print(create_heap(nums))
