# Key idea: Track the active range and the condition that moves its boundaries.
# Compute or update the max subarray same num result for the supplied input.
def max_subarray_same_num(nums):
    L = 0
    window = []
    max_length = 0
    # Process each value from `range(len(nums))`.
    for R in range(len(nums)):
        # Choose this path when `nums[L] == nums[R]` is true.
        if nums[L] == nums[R]:
            window.append(nums[R])
        else:
            L = R
            window = [nums[R]]

        max_length = max(max_length, len(window))

    return max_length

nums = [4,2,2,3,3,3]
print(max_subarray_same_num(nums))    

"""
T(n) = O(n)
S(n) = O(n)

If nums[L] != nums[R]: L = R

Pattern: Sliding window
"""