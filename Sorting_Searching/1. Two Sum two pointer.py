
# Sort values and move two pointers toward the target, then try to recover original indices.
# Sorting mutates numbers and dominates the expected O(n log n) time.
def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    #nums = numbers.copy()
    hashmap = {}
    for i in range(len(numbers)):
        # Only the last original index per value survives; this loses separate indices for duplicate values.
        hashmap[numbers[i]] = i

    numbers.sort()
    #print(nums)
    #print(numbers)
    n = len(numbers)
    low = 0
    high = n - 1
    result = [-1,-1]
    while(low != high):
        # A high sum needs a smaller right value; a low sum needs a larger left value.
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
        # This special case handles all-equal arrays, but not equal-value pairs in otherwise mixed arrays.
        if len(np.unique(numbers)) == 1:
            return [high -1, high]
        elif low == high:
            return [high-1,high]
        else:
            # If both matched values are equal, this can return the same original index twice.
            # The algorithm therefore does not correctly recover distinct indices for every duplicate case.
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