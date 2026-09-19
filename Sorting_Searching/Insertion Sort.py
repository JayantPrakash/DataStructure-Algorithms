def insertionSort(array):
    # Write your code here.
    for i in range(1,len(array)):

        curr_elem = array[i]
        j = i - 1
        while j >= 0 and curr_elem < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j+1] = curr_elem

    return array


array = [6,4,3,8,5]
print(insertionSort(array))

# check the condition for 1st element, j>=0.
#Tn = O(n^2)
#Sn = O(n)
