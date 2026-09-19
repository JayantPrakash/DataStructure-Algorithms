
def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    #nums = numbers.copy()
    hashmap = {}
    for i in range(len(numbers)):
        hashmap[numbers[i]] = i

    numbers.sort()
    #print(nums)
    #print(numbers)
    n = len(numbers)
    low = 0
    high = n - 1
    result = [-1,-1]
    while(low != high):
        if numbers[low] + numbers[high] > target:
            high -= 1
        elif numbers[low] + numbers[high] < target:
            low += 1
        else:
            result = [low,high]
            break

    #print(low,high)
    #print(hashmap)
    if result != [-1,-1]:
        if len(np.unique(numbers)) == 1:
            return [high -1, high]
        elif low == high:
            return [high-1,high]
        else:
            return [hashmap[numbers[low]],hashmap[numbers[high]]]
    else:
        return result

import numpy as np
numbers = [5,3,10,7,1]
#numbers = [4, 1, 5, 0, -1]
#numbers = [5,5,5,5,5,5,5,5]
numbers = [5, 3, 10, 45, 1]
print(two_sum(numbers,6))
#print(len(np.unique(numbers)))