# Key idea: Track complements or pointer movement while avoiding repeated work.
# Compute or update the two sum result for the supplied input.
def two_sum(nums,target):

    my_set = set()

    # Process each value from `range(len(nums))`.
    for i in range(len(nums)):
        # Choose this path when `target - nums[i] in my_set` is true.
        if target - nums[i] in my_set:
            return True
        else:
            my_set.add(nums[i])

    return False

nums = [1,2,6,9,10]

print(two_sum(nums,target=8))
