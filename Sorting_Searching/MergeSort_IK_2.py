def msort(l, start, end):
    if start >= end:
        return

    mid = start + int((end-start)/2)

    msort(l, start, mid)
    msort(l, mid+1, end)

    i = start
    j = mid + 1
    mlist = []
    while i <= mid and j <= end:
        if l[i] < l[j]:
            mlist.append(l[i])
            i += 1
        else:
            mlist.append(l[j])
            j += 1

    while i <=mid:
        mlist.append(l[i])
        i += 1
    while j <=end:
        mlist.append(l[j])
        j += 1

    l[start:end+1] = mlist

    return l

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
