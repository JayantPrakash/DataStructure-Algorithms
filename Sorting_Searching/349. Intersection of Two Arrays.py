class Solution(object):
    # Sort both inputs, then compare their current smallest unprocessed values.
    # Both caller lists are mutated; sorting and linear result-membership checks add to scan cost.
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = len(nums1)
        n = len(nums2)
        i=0
        j=0
        nums1.sort()
        nums2.sort()
        result = []
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                # Deduplicate output using a list search, which is O(r) for r retained values, not O(1).
                if nums1[i] not in result:
                    result.append(nums1[i])
                i += 1
                j += 1
            # Discard the smaller value: it cannot match this or any later value in the other sorted list.
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
        # The two-pointer scan is O(m+n), but repeated list deduplication can make total work quadratic.
        return result

sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sol.intersection(nums1,nums2))

print(set(nums2))


