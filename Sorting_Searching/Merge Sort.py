def merge(S1, S2, S):
    i = j = 0

    while i + j < len(S):
        if j == len(S2) or (i <len(S1) and S1[i] <= S2[j] ):
            S[i+j] = S1[i]
            i = i + 1
        else:
            S[i+j] = S2[j]
            j = j + 1
    return S
def mergeSort(S):
    # Write your code here.
    n = len(S)
    if n < 2:
        return n
    mid = int(n/2)

    S1 = S[0:mid]
    S2 = S[mid:n]

    mergeSort(S1)
    mergeSort(S2)
    return merge(S1,S2,S)


array = [6, 4, 3, 8, 5]
#array = [1]
print(mergeSort(array))
