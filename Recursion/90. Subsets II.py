class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums.sort()
        self.helper(nums,0,[])
        return self.result

    def helper(self, S, i, slate):
        if i == len(S):
            self.result.append(slate[:])
            return
        count = 0
        for index in range(i,len(S)):
            if S[index]!= S[i]:
                break
            count += 1

        self.helper(S, i + count, slate)
        # manager will decide all the duplicate items of one type and pass them to subordinate,
        #subordinate will take decision on other items
        for c in range(0,count):
            slate.append(S[i])
            self.helper(S,i+count,slate)

        for c in range(0,count):
            slate.pop()



sol = Solution()
nums = [1,2,2]
print(sol.subsetsWithDup(nums))

# space and time complexity will be same as subsets with mutable slate