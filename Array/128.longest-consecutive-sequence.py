# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import List
# Group the state and operations used by the longest consecutive sequence implementation.
class Solution:
    # Compute or update the longest consecutive result for the supplied input.
    def longestConsecutive(self, nums: List[int]) -> int:
        set_elems = set(nums)
        longest_seq = 0
        # Process each value from `nums`.
        for num in nums:
            # Choose this path when `num - 1 not in set_elems` is true.
            if num - 1 not in set_elems:
                curr_val = num
                length = 1
                # Keep processing while `curr_val + 1 in set_elems` remains true.
                while (curr_val + 1) in set_elems:
                    curr_val += 1
                    length += 1

                longest_seq = max(length, longest_seq)
        return longest_seq
        

sol = Solution()
nums = [100,4,200,1,3,2]
nums = [1,0,1,2]
nums = [0,3,7,2,5,8,4,6,0,1]
#nums = []
print(sol.longestConsecutive(nums))