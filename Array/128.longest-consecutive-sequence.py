from typing import List
class Solution:
    # A sequence can be counted from its smallest value: it has no predecessor in the set.
    # Membership is expected O(1); the set uses O(n) space.
    def longestConsecutive(self, nums: List[int]) -> int:
        set_elems = set(nums)
        longest_seq = 0
        # This iterates nums rather than the set: duplicate sequence starts repeat the same walk.
        # Unlike the usual unique-start version, this implementation can take O(n^2) time.
        for num in nums:
            # Values with a predecessor belong to a sequence counted from an earlier value.
            if num - 1 not in set_elems:
                curr_val = num
                length = 1
                # Extend by numeric adjacency, not by adjacency in the original array.
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