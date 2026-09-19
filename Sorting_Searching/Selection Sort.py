# Key idea: Track the boundary between the sorted and unsorted portions.
# Compute or update the selection sort result for the supplied input.
def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        min = i
        # Process each value from `range(i + 1, len(array))`.
        for inner in range(i + 1, len(array)):
            # Choose this path when `array[min] > array[inner]` is true.
            if array[min] > array[inner]:
                min = inner

        temp = array[i]
        array[i] = array[min]
        array[inner] = temp


    return array
array = [2,5,4,10,7]