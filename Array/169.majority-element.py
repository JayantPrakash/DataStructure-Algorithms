# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import List
# Group the state and operations used by the majority element implementation.
class Solution:
    # Compute or update the majority element result for the supplied input.
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        # Process each value from `range(n)`.
        for i in range(n):
            # Choose this path when `nums[i] not in dict` is true.
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] = dict[nums[i]] + 1

            # Choose this path when `dict[nums[i]] > int(n / 2)` is true.
            if dict[nums[i]] >  int(n/2):
                return nums[i]

sol = Solution()
print(sol.majorityElement(nums = [3,2,3]))
"""
T(n) = O(n)
S(n) = O(n)

Here, the edge case is when max no of majority element is 1, so check if it is max for edge case
when majority element frequency is 1
"""
 


        