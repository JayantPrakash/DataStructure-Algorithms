# Key idea: Follow pointer updates carefully so links are neither skipped nor lost.
# Compute or update the k smallest number result for the supplied input.
def k_smallest_number(lists, k):
    # Replace this placeholder return statement with your code

    m = len(lists)
    # Choose this path when `m == 0` is true.
    if m == 0:
        return 0
    # Choose this path when `m == 1` is true.
    if m == 1:
        # Choose this path when `k - 1 < len(lists[0])` is true.
        if k -1 < len(lists[0]):
            return lists[0][k-1]
        else:
            return lists[0][-1]

    final_list = lists[0]

    # Process each value from `range(m)`.
    for i in range(m):
        list1 = final_list
        list2 = lists[i + 1]

        final_list = merge(list1, list2)

        # Choose this path when `i + 1 == m - 1` is true.
        if i + 1 == m - 1:
            break

    # Choose this path when `k > len(final_list) - 1` is true.
    if k > len(final_list) - 1:
        return final_list[-1]

    return final_list[k - 1]


# Compute or update the merge result for the supplied input.
def merge(list1, list2):
    i = 0
    j = 0
    mid = len(list1) - 1
    end = len(list2) - 1
    mlist = []
    # Keep processing while `i <= mid and j <= end` remains true.
    while i <= mid and j <= end:
        # Choose this path when `list1[i] > list2[j]` is true.
        if list1[i] > list2[j]:
            mlist.append(list2[j])
            j += 1
        else:
            mlist.append(list1[i])
            i += 1

    # Keep processing while `i <= mid` remains true.
    while i <= mid:
        mlist.append(list1[i])
        i += 1

    # Keep processing while `j <= end` remains true.
    while j <= end:
        mlist.append(list2[j])
        j += 1

    return mlist

lists = [[2, 6, 8], [3, 7, 10], [5, 8, 11]]
#lists = []
#lists = [[1]]
k = 15
print(k_smallest_number(lists, 15))