# Sort inclusive range start..end by splitting until singleton ranges, then merging sorted halves.
# O(n log n) time, O(n) temporary merge storage, and O(log n) recursion depth.
def msort(l, start, end):
    if start >= end:
        return

    mid = start + int((end-start)/2)

    # Both halves must be sorted before the parent compares their smallest unconsumed values.
    msort(l, start, mid)
    msort(l, mid+1, end)

    i = start
    j = mid + 1
    mlist = []
    while i <= mid and j <= end:
        # Ties are taken from the right half in this version, so relative order of equal-key records is not stable.
        if l[i] < l[j]:
            mlist.append(l[i])
            i += 1
        else:
            mlist.append(l[j])
            j += 1

    # Copy any leftover suffix after one half is exhausted; no further comparisons are needed.
    while i <=mid:
        mlist.append(l[i])
        i += 1
    while j <=end:
        mlist.append(l[j])
        j += 1

    # Write the merged values back into exactly the original range so other ranges remain intact.
    l[start:end+1] = mlist

    return l

# The wrapper returns None for length 0 or 1 because the helper's base case has a bare return.
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
