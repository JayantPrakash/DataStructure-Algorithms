# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import Optional, List
# Group the state and operations used by the contains optimized implementation.
class Solution:
    # Compute or update the contains duplicate result for the supplied input.
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        # Process each value from `nums`.
        for num in nums:
            # Choose this path when `num in seen` is true.
            if num in seen:
                return True
            seen.add(num)

        return False     
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))    
print(sol.containsDuplicate([1,2,3,4]))
                

        