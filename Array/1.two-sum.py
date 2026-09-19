from typing import Optional, List
class Solution:
    # Use a value-to-index lookup to find target - nums[i] without a nested scan.
    # Two passes take expected O(n) time and O(n) space.
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        # Keep the last index for each value; duplicates overwrite earlier indices.
        for i, key in enumerate(nums):
            dict[key] = i 

        # Search the original list, so duplicate values still have distinct candidate indices.
        for i in range(len(nums)):
            remain_val = target - nums[i]

            # Reject pairing an element with itself; [3, 3] still works because indices differ.
            if (remain_val in dict.keys()) and (i != dict[remain_val]):
                return([i, dict[remain_val]])

        return []    

sol = Solution()

#print(sol.twoSum(nums = [2,7,11,15], target = 9))
#print(sol.twoSum(nums = [3,2,4], target = 6))
print(sol.twoSum(nums = [3,3], target = 6))


"""
Since here dict gets updated with duplicate value,
make sure to access the items in dict with nums[i],rather than
iterating through dict. We use this approach as duplicate dict value will
get updated with recent value of dict.

T(n) = O(n)
S(n) = O(n)
"""

        