# Key idea: Track the active range and the condition that moves its boundaries.
from typing import List
# Group the state and operations used by the minimum size subarray sum implementation.
class Solution:
    # Compute or update the min sub array len result for the supplied input.
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, L = 0, 0
        min_length = float("inf")
        # Process each value from `range(len(nums))`.
        for R in range(len(nums)):
            total += nums[R]

            # Keep processing while `total >= target` remains true.
            while total >= target:
                min_length = min(R-L+1, min_length)
                total -= nums[L]
                L += 1
    
        # Choose this path when `min_length == float('inf')` is true.
        if min_length == float("inf"): return 0
        return min_length

sol = Solution()
target = 7
nums = [2,3,1,2,4,3]  

target = 4
nums = [1,4,4]

target = 11
nums = [1,1,1,1,1,1,1,1]
"""
nums = [1,2,3,4,5]
target = 11
"""
print(sol.minSubArrayLen(target, nums))  

"""
T(n) = O(n)
S(n) = O(1)
"""