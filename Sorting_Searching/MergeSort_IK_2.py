# Key idea: Follow the divide, recursive sort, and merge phases.
# Compute or update the msort result for the supplied input.
def msort(l, start, end):
    # Choose this path when `start >= end` is true.
    if start >= end:
        return

    mid = start + int((end-start)/2)

    msort(l, start, mid)
    msort(l, mid+1, end)

    i = start
    j = mid + 1
    mlist = []
    # Keep processing while `i <= mid and j <= end` remains true.
    while i <= mid and j <= end:
        # Choose this path when `l[i] < l[j]` is true.
        if l[i] < l[j]:
            mlist.append(l[i])
            i += 1
        else:
            mlist.append(l[j])
            j += 1

    # Keep processing while `i <= mid` remains true.
    while i <=mid:
        mlist.append(l[i])
        i += 1
    # Keep processing while `j <= end` remains true.
    while j <=end:
        mlist.append(l[j])
        j += 1

    l[start:end+1] = mlist

    return l

# Compute or update the merge sort result for the supplied input.
def MergeSort(A):
    res = msort(A, 0, len(A) - 1)
    return res


A = [6, 4, 3, 8, 1, 5, 2, 7, 22, 15, 0]
A = [6, 4, 3, 8, 1, 5, 2, 7]
print(MergeSort(A))

"""
Note:
base start >= end:
    return 
return l in msort
mid = start + int((end-start)/2)

T(n) = O(nlogn)
S(n) = O(n)
"""
