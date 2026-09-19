# Merge two sorted slices into S; i+j is exactly the number of values already written.
def merge(S1, S2, S):
    i = j = 0

    while i + j < len(S):
        # Choose left when right is exhausted or left is no greater; ties from the left preserve stability.
        if j == len(S2) or (i <len(S1) and S1[i] <= S2[j] ):
            S[i+j] = S1[i]
            i = i + 1
        else:
            S[i+j] = S2[j]
            j = j + 1
    return S
# Divide, sort both halves recursively, and merge: O(n log n) time with O(n) peak auxiliary storage.
def mergeSort(S):
    n = len(S)
    # The slice is already sorted; this version returns its length rather than the list in this base case.
    if n < 2:
        return n
    mid = int(n/2)

    S1 = S[0:mid]
    S2 = S[mid:n]

    # Recursive calls mutate their slices; merging those sorted slices writes back into S.
    mergeSort(S1)
    mergeSort(S2)
    return merge(S1,S2,S)


array = [6, 4, 3, 8, 5]
#array = [1]
print(mergeSort(array))
