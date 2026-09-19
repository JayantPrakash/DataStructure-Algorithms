from collections import defaultdict
# Despite the filename, this is an unfinished two-sum experiment, not a three-sum implementation.
def twoSum(nums,target):

    dict = {}
    for i in range(len(nums)):
        # dict is a dictionary and has no append method; nonempty input stops here with AttributeError.
        dict.append(i)

    i = 0
    j = len(nums) - 1

    # If the setup were corrected, sorting would support a two-pointer pair search.
    nums.sort()
    #for k in range(1,len(nums)):
    while i < j:
        if nums[i] + nums[j] == target:
            return True

        # For sorted input, a low sum moves the left pointer up; a high sum moves the right pointer down.
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