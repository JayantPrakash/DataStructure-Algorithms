# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
# Group the state and operations used by the two sum implementation.
class Solution(object):
    # Compute or update the two sum result for the supplied input.
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {}

        # Process each value from `enumerate(nums)`.
        for i, key in enumerate(nums):
            dict[key] = i

        l, r = 0, len(nums) - 1
        # Process each value from `range(len(nums))`.
        for i in range(len(nums)):
            remain_val = target - nums[i]

            # Choose this path when `remain_val in dict and dict[remain_val] != i` is true.
            if remain_val in dict and dict[remain_val] !=i:
                return [i, dict[remain_val]]

nums = [2,7,11,15]
target = 9
#nums = [3,3]
#target = 6
sol = Solution()
print(sol.twoSum(nums, target))