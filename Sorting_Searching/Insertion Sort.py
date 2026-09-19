# Maintain a sorted prefix and insert each next value into its correct position.
# O(n^2) worst-case time, O(n) best case, O(1) auxiliary space; this mutates the input.
def insertionSort(array):
    for i in range(1,len(array)):

        # Save the candidate because shifting larger values will overwrite its original slot.
        curr_elem = array[i]
        j = i - 1
        # Move larger prefix values right until a gap opens; strict comparison preserves equal-value order.
        while j >= 0 and curr_elem < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # j stopped before the insertion position, so put the saved value in j+1.
        array[j+1] = curr_elem

    return array


array = [6,4,3,8,5]
print(insertionSort(array))

# check the condition for 1st element, j>=0.
#Tn = O(n^2)
