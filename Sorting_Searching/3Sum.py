from collections import defaultdict
def twoSum(nums,target):

    # default dict list used to counter duplicate element cases
    dict = {}
    for i in range(len(nums)):
        dict.append(i)

    i = 0
    j = len(nums) - 1

    nums.sort()
    #for k in range(1,len(nums)):
    while i < j:
        if nums[i] + nums[j] == target:
            return True

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