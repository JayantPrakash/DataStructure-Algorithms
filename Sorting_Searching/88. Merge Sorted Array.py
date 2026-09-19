# Key idea: Follow the divide, recursive sort, and merge phases.
from typing import List
# Group the state and operations used by the Merge Sorted Array implementation.
class Solution:
    # Compute or update the merge result for the supplied input.
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1 = m - 1
        p2 = n - 1

        # Process each value from `range(n + m - 1, -1, -1)`.
        for p in range(n + m - 1, -1, -1):
            # Choose this path when `p2 < 0` is true.
            if p2 < 0:
                break
            # Choose this path when `p1 >= 0 and nums1[p1] > nums2[p2]` is true.
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        return nums1


nums1 = [23, 33, 35, 41, 44, 47, 56, 91, 105, 0, 0, 0, 0, 0, 0]
nums2 = [32, 49, 50, 51, 61, 99]

sol = Solution()

print(sol.merge(nums1, 9, nums2, 6))
