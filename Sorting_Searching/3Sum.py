# Key idea: Track complements or pointer movement while avoiding repeated work.
from collections import defaultdict
# Compute or update the two sum result for the supplied input.
def twoSum(nums,target):

    # default dict list used to counter duplicate element cases
    dict = {}
    # Process each value from `range(len(nums))`.
    for i in range(len(nums)):
        dict.append(i)

    i = 0
    j = len(nums) - 1

    nums.sort()
    #for k in range(1,len(nums)):
    while i < j:
        # Choose this path when `nums[i] + nums[j] == target` is true.
        if nums[i] + nums[j] == target:
            return True

        # Choose this path when `nums[i] + nums[j] < target` is true.
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return False
nums = [2,7,11,15]
target = 9

numbers = [3,24,50,79,88,150,345]
target = 200

numbers = [3,2,3]
target = 6
print(twoSum(numbers,target))

"""
T(n) = O(nlogn)
S(n) = O(n)
"""