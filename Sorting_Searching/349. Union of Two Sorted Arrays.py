class Solution(object):
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
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
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

