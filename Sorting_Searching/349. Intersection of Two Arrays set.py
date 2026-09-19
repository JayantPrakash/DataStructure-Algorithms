class Solution(object):
    # Sets remove duplicates before membership tests; the intersection contains each common value once.
    # Building both sets takes expected O(m+n) time/space, and output order is unspecified.
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        # Scan one set and retain values found in the other using expected O(1) membership.
        def set_intersection(n1,n2):
            return [x for x in n1 if x in n2]

        # This branch scans the larger set, though scanning the smaller set would reduce lookup count.
        if len(nums1) >= len(nums2):
            return set_intersection(nums1,nums2)
        else:
            return set_intersection(nums2, nums1)

sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sol.intersection(nums1,nums2))

print(set(nums2))


