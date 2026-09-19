from typing import List
class Solution:
    # For index i, multiply everything strictly left of i by everything strictly right of i.
    # No division is needed, so zeros work naturally; O(n) time and O(n) auxiliary space.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_arr = len(nums)
        # One is the identity for multiplication and handles the empty product at each boundary.
        prefix = [1] * len_arr
        suffix = [1] * len_arr
        j = len_arr - 2
        # Build exclusive prefix products left-to-right and exclusive suffix products right-to-left.
        for i in range(1,len_arr):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[j] = suffix[j+1] * nums[j+1]
            j = j - 1

        ans = [1] * len_arr
        for i in range(len_arr):
            # Both factors exclude nums[i], so their product contains every other element exactly once.
            ans[i] = prefix[i] * suffix[i]

        return ans     

sol = Solution()
nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
print(sol.productExceptSelf(nums))