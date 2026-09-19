def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        min = i
        for inner in range(i + 1, len(array)):
            if array[min] > array[inner]:
                min = inner

        temp = array[i]
        array[i] = array[min]
        array[inner] = temp


    return array
array = [2,5,4,10,7]