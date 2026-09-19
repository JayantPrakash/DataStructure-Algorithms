# Key idea: Track how values move toward their final sorted positions.
# Group the state and operations used by the Intersection of Two Arrays implementation.
class Solution(object):
    # Compute or update the intersection result for the supplied input.
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
        # Keep processing while `i < m and j < n` remains true.
        while i < m and j < n:
            # Choose this path when `nums1[i] == nums2[j]` is true.
            if nums1[i] == nums2[j]:
                # Choose this path when `nums1[i] not in result` is true.
                if nums1[i] not in result:
                    result.append(nums1[i])
                i += 1
                j += 1
            # Choose this path when `nums1[i] < nums2[j]` is true.
            elif nums1[i] < nums2[j]:
                i += 1
            # Choose this path when `nums2[j] < nums1[i]` is true.
            elif nums2[j] < nums1[i]:
                j += 1
        return result

sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sol.intersection(nums1,nums2))

print(set(nums2))

#T(n) = O(max(m,n))
#S(n) = O(min(m,n))

