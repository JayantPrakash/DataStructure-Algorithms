from typing import List
class Solution:
    # Count occurrences until one value exceeds half the entire array length.
    # Expected O(n) time and O(n) space; the problem guarantees a majority exists.
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        for i in range(n):
            # First occurrences start at one; later occurrences increment the same counter.
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] = dict[nums[i]] + 1

            # A strict majority cannot be overtaken by all remaining values combined, so return immediately.
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
 


        