def twoSum(nums,target):
    nums.sort()
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            return [i+1,j+1]
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1

nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

numbers = [-1,0]
target = -1

numbers = [2,3,4]
target = 6

numbers = [2,7,11,15]
target = 9

numbers = [3,24,50,79,88,150,345]
target = 200

print(twoSum(numbers,target))