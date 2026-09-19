# Key idea: Follow the divide, recursive sort, and merge phases.
# Compute or update the merge result for the supplied input.
def merge(S1, S2, S):
    i = j = 0

    # Keep processing while `i + j < len(S)` remains true.
    while i + j < len(S):
        # Choose this path when `j == len(S2) or (i < len(S1) and S1[i] <= S2[j])` is true.
        if j == len(S2) or (i <len(S1) and S1[i] <= S2[j] ):
            S[i+j] = S1[i]
            i = i + 1
        else:
            S[i+j] = S2[j]
            j = j + 1
    return S
# Compute or update the merge sort result for the supplied input.
def mergeSort(S):
    # Write your code here.
    n = len(S)
    # Choose this path when `n < 2` is true.
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
