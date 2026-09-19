def bubbleSort(array):
    # Write your code here.
    for i in range(len(array)):
        for inner in range(len(array)-1, i,-1):
            print(inner)
            if array[inner] < array[inner - 1]:
                temp = array[inner]
                array[inner] = array[inner - 1]
                array[inner - 1] = temp
    return array


array = [2, 5, 3, 10, 1]
print(bubbleSort(array))
#print(range(5, 3))
for inner in range(len(array)-1,0,-1):
    print(inner)