# Key idea: Track how values move toward their final sorted positions.
# Group the state and operations used by the Intersection of Two Arrays set implementation.
class Solution(object):
    # Compute or update the intersection result for the supplied input.
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        # Compute or update the set intersection result for the supplied input.
        def set_intersection(n1,n2):
            return [x for x in n1 if x in n2]

        # Choose this path when `len(nums1) >= len(nums2)` is true.
        if len(nums1) >= len(nums2):
            return set_intersection(nums1,nums2)
        else:
            return set_intersection(nums2, nums1)

sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sol.intersection(nums1,nums2))

print(set(nums2))


