from typing import List
class Solution:
    # Merge backward into nums1's reserved capacity to avoid overwriting unread values.
    # O(m+n) time and O(1) auxiliary space; this version also returns the mutated nums1.
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # p1/p2 identify the largest unread value in each sorted input; p is the next destination from the end.
        p1 = m - 1
        p2 = n - 1

        for p in range(n + m - 1, -1, -1):
            # Once nums2 is exhausted, any remaining nums1 prefix is already correctly positioned.
            if p2 < 0:
                break
            # Write the larger remaining value at p; if nums1 is exhausted, copy from nums2.
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
