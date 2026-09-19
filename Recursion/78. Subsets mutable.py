class Solution(object):
    #def __init__(self):
    #    self.result = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []

        self.helper(nums, 0, [])
        return self.result

    def helper(self, S, i, slate):
        if i == len(S):
            self.result.append(slate[:])
            return
        else:
            self.helper(S, i + 1, slate)
            slate.append(S[i])
            self.helper(S, i + 1, slate)
            slate.pop()


nums = [1, 2, 3]

sol = Solution()
print(sol.subsets(nums))

#s(n) = i/p + intermediate + o/p
#ip -n, intermediate - O(n) - there is only one copy of slate
# o/p - O(2^n*n/2) - no of leaf nodes - 2^n, average length of leaf is n/2. No of elements in left side
# has complimentary number of elements in right side. For ex - {1} and {2,3} are complimentary
#S(n) - O(2^n*n)

#T(n) - O(2^n* 1) - internal node, leaf node - O(2^n*)n/2
# - *n/2  as for each leaf node, slate is copied and added to result(avg length of leaf is n/2)
#T(n) - O(2^n*n)

