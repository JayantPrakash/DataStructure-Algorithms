class Solution(object):
    # Build a value-to-index map, then search each value's complement in expected O(n) time/O(n) space.
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {}

        # Duplicate values retain their last index; scanning nums afterward still permits pairs like [3, 3].
        for i, key in enumerate(nums):
            dict[key] = i

        l, r = 0, len(nums) - 1
        for i in range(len(nums)):
            remain_val = target - nums[i]

            # Distinct indices are required, so the current element cannot supply its own complement.
            if remain_val in dict and dict[remain_val] !=i:
                return [i, dict[remain_val]]

nums = [2,7,11,15]
target = 9
#nums = [3,3]
#target = 6
sol = Solution()
print(sol.twoSum(nums, target))