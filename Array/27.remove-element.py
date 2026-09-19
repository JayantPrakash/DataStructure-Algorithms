from typing import List
class Solution:
    # Remove matches by shifting the list and appending a placeholder to keep its length fixed.
    # Repeated pop(i) shifts can make this O(n^2); the final slice also allocates O(n) space.
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        len_list = len(nums)
        i = 0
        while i < len_list:
            # Do not advance i after removal: the next unexamined value has shifted into this index.
            if val == nums[i]:
                nums.pop(i)
                nums.append("_")
            else: 
                # Count surviving values but exclude padding; the input is assumed to contain integers.
                if nums[i] != "_":  
                    ans += 1
                i += 1
        # This slice rebinds only the local name; it does not shorten the caller's already-mutated list.
        # It also includes an extra slot; callers should use the returned survivor count.
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