# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import List
# Group the state and operations used by the remove element implementation.
class Solution:
    # Compute or update the remove element result for the supplied input.
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        len_list = len(nums)
        i = 0
        # Keep processing while `i < len_list` remains true.
        while i < len_list:
            # Choose this path when `val == nums[i]` is true.
            if val == nums[i]:
                nums.pop(i)
                nums.append("_")
            else: 
                # Choose this path when `nums[i] != '_'` is true.
                if nums[i] != "_":  
                    ans += 1
                i += 1
        nums = nums[0:ans+1]        

        return ans  


sol = Solution()
print(sol.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))        

"""
T(n) = O(n)
S(n) = O(1)

Here, we should add "_" at the end if val is matched and check if "_" is not there,
when incrementing ans as we unnecssarily inscrease the ans counter
"""