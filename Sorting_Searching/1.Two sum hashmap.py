def two_sum(nums,target):

    my_set = set()

    for i in range(len(nums)):
        if target - nums[i] in my_set:
            return True
        else:
            my_set.add(nums[i])

    return False

nums = [1,2,6,9,10]

print(two_sum(nums,target=8))
