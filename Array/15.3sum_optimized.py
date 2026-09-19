# Key idea: Track complements or pointer movement while avoiding repeated work.
from typing import List
# Group the state and operations used by the 3sum optimized implementation.
class Solution:
    # Compute or update the three sum result for the supplied input.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Compute or update the two sum result for the supplied input.
        def twoSum(l,r, target):

            # Keep processing while `l < r` remains true.
            while l < r:
                # Choose this path when `nums[l] + nums[r] + target == 0` is true.
                if nums[l] + nums[r] + target == 0:
                    ans.append([target,nums[l],nums[r]])
                    l += 1  
                    r -= 1 
                    # Keep processing while `nums[l] == nums[l - 1] and l < r` remains true.
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
                # Choose this path when `nums[l] + nums[r] + target < 0` is true.
                if nums[l] + nums[r] + target < 0:
                    l += 1
                # Choose this path when `nums[l] + nums[r] + target > 0` is true.
                if nums[l] + nums[r] + target > 0:
                    r -= 1

            return 
        
        nums.sort()
        ans = []
        # Process each value from `range(len(nums) - 2)`.
        for i in range(len(nums) - 2):
            # Choose this path when `nums[i] > 0` is true.
            if nums[i] > 0:
                break
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            # Choose this path when `i == 0 or nums[i - 1] != nums[i]` is true.
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(left,right, target)
        return ans