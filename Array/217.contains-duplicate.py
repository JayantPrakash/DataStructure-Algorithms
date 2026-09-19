# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import Optional, List
# Group the state and operations used by the contains duplicate implementation.
class Solution:
    # Compute or update the contains duplicate result for the supplied input.
    def containsDuplicate(self, nums: List[int]) -> bool:

        dict = {}

        # Process each value from `enumerate(nums)`.
        for i, elem in enumerate(nums):
            # Choose this path when `elem not in dict.keys()` is true.
            if elem not in dict.keys():
                dict[elem] = i
            else:
                return True

        return False    
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))    
print(sol.containsDuplicate([1,2,3,4]))
                

        