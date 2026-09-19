# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import List
# Group the state and operations used by the concatenation of array implementation.
class Solution:
    # Compute or update the get concatenation result for the supplied input.
    def getConcatenation(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)
        ans = [0] * 2 * len_nums
        j = 0

        # Process each value from `range(len(ans))`.
        for i in range(len(ans)):
            # Choose this path when `len_nums > i` is true.
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

        