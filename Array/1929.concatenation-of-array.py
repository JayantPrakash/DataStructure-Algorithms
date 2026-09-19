from typing import List
class Solution:
    # Build an output of length 2n: the first and second halves both reproduce nums.
    # O(n) time and O(n) output space.
    def getConcatenation(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)
        ans = [0] * 2 * len_nums
        j = 0

        for i in range(len(ans)):
            # The first half uses its output index directly; j restarts input indexing for the second half.
            if len_nums > i:
                ans[i] = nums[i]
            else:
                ans[j + len_nums] = nums[j]
                j += 1    

        return ans     
    
sol = Solution()
print(sol.getConcatenation(nums = [1,2,1]))   

"""
T(n) = O(n)
S(n) = O(n)
"""

        