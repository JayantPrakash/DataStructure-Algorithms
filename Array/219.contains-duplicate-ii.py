# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import List
# Group the state and operations used by the contains duplicate ii implementation.
class Solution:
    # Compute or update the contains nearby duplicate result for the supplied input.
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        # Process each value from `range(len(nums))`.
        for R in range(len(nums)):
            # Choose this path when `R - L > k` is true.
            if R - L > k:
                window.remove(nums[L])
                L += 1

            # Choose this path when `nums[R] in window` is true.
            if nums[R] in window:
                return True

            window.add(nums[R])

        return False

sol = Solution()
nums = [1,2,3,1]
k = 3

nums = [1,0,1,1]
k = 1

nums = [1,2,3,1,2,3]
k = 2
print(sol.containsNearbyDuplicate(nums,k))            