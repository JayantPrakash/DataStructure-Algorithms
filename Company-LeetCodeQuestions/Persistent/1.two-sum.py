class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {}

        for i, key in enumerate(nums):
            dict[key] = i

        l, r = 0, len(nums) - 1
        for i in range(len(nums)):
            remain_val = target - nums[i]

            if remain_val in dict and dict[remain_val] !=i:
                return [i, dict[remain_val]]

nums = [2,7,11,15]
target = 9
#nums = [3,3]
#target = 6
sol = Solution()
print(sol.twoSum(nums, target))