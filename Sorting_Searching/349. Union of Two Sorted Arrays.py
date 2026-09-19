class Solution(object):
    # Merge two already-sorted lists, advancing the side with the smaller current value.
    # O(m+n) time and output space; input order is preserved.
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
        while i < m and j < n:
            # Equal heads are emitted once and both pointers advance.
            # Repeated copies within an input are not fully removed, so this is not always a distinct-value set union.
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                result.append(nums2[j])
                j += 1
        # Once one list is exhausted, append the other's already-sorted remainder.
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        # Handle the symmetric case where nums1 was exhausted first.
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

