import random
# Randomized in-place partitioning: expected O(n log n) time, worst-case O(n^2).
# Recursion uses expected O(log n) stack space, worst-case O(n); tiny inputs return None here.
def quicksort(a):
    return qsort(a,0,len(a)-1)

def qsort(l,start,end):

    if start >= end:
        return

    # Randomize the pivot to reduce dependence on input order; many equal values can still cause skewed splits.
    rand_index = random.randint(start,end)
    l[start],l[rand_index] = l[rand_index], l[start]

    pivot = l[start]
    smaller = start
    bigger = start
    # Before each test, l[start+1:smaller+1] is <= pivot and l[smaller+1:bigger] is > pivot.
    for bigger in range(start+1, end+1):
        if l[bigger] <= pivot:
            # Extend the small-value region and swap the new qualifying element into it.
            smaller += 1
            l[smaller],l[bigger] = l[bigger], l[smaller]

    # Only after the scan, place the pivot between the two regions; its position is now final.
    l[smaller],l[start] = l[start],l[smaller]

    # Exclude the fixed pivot and independently sort the two remaining regions.
    qsort(l,start, smaller-1)
    qsort(l,smaller+1, end)

    return l

array = [4, 2, 8, 7, 1, 3, 5, 6]
print(quicksort(array))

"""
Here, l[smaller] will always be smaller than pivot and
l[bigger] will always be bigger than pivot

if pivot is median
best case - T(n) = cn + T(n/2) + T(n/2) = O(nlogn)

worst case : If smallest or largest element is selected always,
split will be extremely skewed
T(n) = cn + T(n-1) = O(n^2)

"""
