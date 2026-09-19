# Key idea: Track how values move toward their final sorted positions.
# Group the state and operations used by the Union of Two Sorted Arrays implementation.
class Solution(object):
    # Compute or update the union result for the supplied input.
    def Union(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = len(nums1)
        n = len(nums2)
        i=0
        j=0
        result = []
        # Keep processing while `i < m and j < n` remains true.
        while i < m and j < n:
            # Choose this path when `nums1[i] == nums2[j]` is true.
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            # Choose this path when `nums1[i] < nums2[j]` is true.
            elif nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            # Choose this path when `nums2[j] < nums1[i]` is true.
            elif nums2[j] < nums1[i]:
                result.append(nums2[j])
                j += 1
        # Keep processing while `i < len(nums1)` remains true.
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        # Keep processing while `j < len(nums2)` remains true.
        while j < len(nums2):
            result.append(nums2[j])
            j += 1


        return result

sol = Solution()
nums1 = [4,5,9]
nums2 = [1,2,7,10]
print(sol.Union(nums1,nums2))



#T(n) = O(max(m,n))
#S(n) = O(max(m,n))

