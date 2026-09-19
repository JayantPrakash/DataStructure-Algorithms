from typing import List
class Solution:
    # Sliding window for positive numbers: extending right increases the sum; removing left decreases it.
    # Each boundary crosses the array once, so O(n) time and O(1) space.
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, L = 0, 0
        min_length = float("inf")
        for R in range(len(nums)):
            # Include the new right endpoint before testing whether the window reaches target.
            total += nums[R]

            # Record every qualifying window, then shrink to seek a shorter one with the same right endpoint.
            while total >= target:
                min_length = min(R-L+1, min_length)
                total -= nums[L]
                L += 1
    
        # Infinity means no window ever reached target; the required no-solution answer is zero.
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