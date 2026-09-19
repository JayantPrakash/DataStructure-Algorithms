from typing import Optional, List
class Solution:
    # Remember values already encountered in a dictionary; the stored index is not needed for detection.
    # Expected O(n) time and O(n) space.
    def containsDuplicate(self, nums: List[int]) -> bool:

        dict = {}

        for i, elem in enumerate(nums):
            # The first occurrence is recorded; a later occurrence proves there is a duplicate.
            if elem not in dict.keys():
                dict[elem] = i
            else:
                return True

        # Only a complete scan without a repeated value establishes uniqueness.
        return False    
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))    
print(sol.containsDuplicate([1,2,3,4]))
                

        