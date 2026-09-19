from typing import Optional, List
class Solution:
    # A set represents exactly the values seen earlier, with no unnecessary index information.
    # Expected O(n) time and O(n) space.
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            # Check before inserting so the current occurrence cannot match itself.
            if num in seen:
                return True
            seen.add(num)

        # Reaching the end means every insertion introduced a new value.
        return False     
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))    
print(sol.containsDuplicate([1,2,3,4]))
                

        