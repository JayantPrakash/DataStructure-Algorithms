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
            hsmap = []
            for pick in range(i,len(S)):
                if S[pick] not in hsmap:
                    #continue
                    S[i],S[pick] = S[pick], S[i]
                    slate.append(S[i])
                    self.helper(S,i+1,slate)
                    slate.pop()
                    S[i],S[pick] = S[pick], S[i]
                    hsmap.append(S[pick])


sol = Solution()
nums = [2,2,1,1]
print(sol.permute(nums))
