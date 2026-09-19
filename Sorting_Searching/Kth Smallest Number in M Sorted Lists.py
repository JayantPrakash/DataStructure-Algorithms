def k_smallest_number(lists, k):
    # Replace this placeholder return statement with your code

    m = len(lists)
    if m == 0:
        return 0
    if m == 1:
        if k -1 < len(lists[0]):
            return lists[0][k-1]
        else:
            return lists[0][-1]

    final_list = lists[0]

    for i in range(m):
        list1 = final_list
        list2 = lists[i + 1]

        final_list = merge(list1, list2)

        if i + 1 == m - 1:
            break

    if k > len(final_list) - 1:
        return final_list[-1]

    return final_list[k - 1]


def merge(list1, list2):
    i = 0
    j = 0
    mid = len(list1) - 1
    end = len(list2) - 1
    mlist = []
    while i <= mid and j <= end:
        if list1[i] > list2[j]:
            mlist.append(list2[j])
            j += 1
        else:
            mlist.append(list1[i])
            i += 1

    while i <= mid:
        mlist.append(list1[i])
        i += 1

    while j <= end:
        mlist.append(list2[j])
        j += 1

    return mlist

lists = [[2, 6, 8], [3, 7, 10], [5, 8, 11]]
#lists = []
#lists = [[1]]
k = 15
print(k_smallest_number(lists, 15))