class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.helper(nums,0,[])
        return self.result

    def helper(self, S, i, slate):
        if i == len(S):
            self.result.append(slate[:])
            return
        else:
            for pick in range(i,len(S)):
                S[i],S[pick] = S[pick], S[i]
                slate.append(S[i])
                self.helper(S,i+1,slate)
                slate.pop()
                S[i],S[pick] = S[pick], S[i]

sol = Solution()
nums = [1,2,3]
print(sol.permute(nums))

