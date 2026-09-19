# Intended selection sort: find the smallest item in the unsorted suffix, then place it at i.
# The intended algorithm uses O(n^2) comparisons and O(1) extra space.
def selectionSort(array):
    for i in range(len(array)):
        # Store the candidate's index, updating it whenever a smaller suffix value is found.
        min = i
        for inner in range(i + 1, len(array)):
            if array[min] > array[inner]:
                min = inner

        temp = array[i]
        array[i] = array[min]
        # This writes to the final scan index, not the selected minimum's index.
        # It can overwrite a different value, and inner is undefined for a singleton input; code is retained as written.
        array[inner] = temp


    return array
array = [2,5,4,10,7]