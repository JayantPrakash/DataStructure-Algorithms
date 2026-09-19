# Sweep right-to-left so each pass bubbles the smallest remaining value to position i.
# O(n^2) comparisons even on sorted input; O(1) extra space.
def bubbleSort(array):
    for i in range(len(array)):
        # The prefix before i is already settled and excluded from this pass.
        for inner in range(len(array)-1, i,-1):
            print(inner)
            # Swap only strictly out-of-order neighbors; equal values keep their relative order, making this stable.
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