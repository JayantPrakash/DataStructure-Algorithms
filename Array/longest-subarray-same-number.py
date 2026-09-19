# Track the current run of equal adjacent values, not a subsequence spread across the array.
# The explicit window list uses O(n) worst-case space; the scan takes O(n) time.
def max_subarray_same_num(nums):
    L = 0
    window = []
    max_length = 0
    for R in range(len(nums)):
        # Matching the run's first value extends the run; a mismatch starts a new run at R.
        if nums[L] == nums[R]:
            window.append(nums[R])
        else:
            L = R
            window = [nums[R]]

        # Save the best run before later mismatches reset the current window.
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