# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import List
# Group the state and operations used by the house robber implementation.
class Solution:
    # Compute or update the rob result for the supplied input.
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        mem = {}
        # Compute or update the helper result for the supplied input.
        def helper(i: int )-> int:
            # Choose this path when `i in mem` is true.
            if i in mem:
                return mem[i]
            # Choose this path when `i == 0` is true.
            if i == 0:
                mem[i] = nums[0]
                return mem[i]
            # Choose this path when `i == 1` is true.
            if i == 1:
                mem[i] = max(nums[0], nums[1]) 
                return mem[i] 
            mem[i] = max(helper(i-2) + nums[i], helper(i-1))
            return mem[i]
        
        return helper(len(nums)-1)       

sol = Solution()
nums = [1,2,3,1]
nums = [2,7,9,3,1]
print(sol.rob(nums))    