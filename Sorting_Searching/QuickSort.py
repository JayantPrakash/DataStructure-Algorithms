import random
def quicksort(a):
    return qsort(a,0,len(a)-1)

def qsort(l,start,end):

    if start >= end:
        return

    rand_index = random.randint(start,end)
    l[start],l[rand_index] = l[rand_index], l[start]

    pivot = l[start]
    smaller = start
    bigger = start
    for bigger in range(start+1, end+1):
        if l[bigger] <= pivot:
            smaller += 1
            l[smaller],l[bigger] = l[bigger], l[smaller]

    l[smaller],l[start] = l[start],l[smaller]

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
