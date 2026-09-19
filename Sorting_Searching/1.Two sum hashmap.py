# Store previous values and ask whether the current value's complement was seen.
# This returns existence, not indices; expected O(n) time and O(n) space.
def two_sum(nums,target):

    my_set = set()

    for i in range(len(nums)):
        # Check before inserting so an element cannot pair with itself; a second equal value can form a valid pair.
        if target - nums[i] in my_set:
            return True
        else:
            my_set.add(nums[i])

    # No complementary pair occurred among any of the distinct input positions.
    return False

nums = [1,2,6,9,10]

print(two_sum(nums,target=8))
