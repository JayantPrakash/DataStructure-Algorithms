class Solution(object):
    # Sort to group equal values, then decide how many copies of each value to include.
    # This avoids duplicate subsets; sorting mutates nums and output can still be exponential.
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
            # Copy the completed subset so later restoration does not alter saved answers.
            self.result.append(slate[:])
            return
        # Measure the run of equal values starting at i; one recursion level decides the whole run.
        count = 0
        for index in range(i,len(S)):
            if S[index]!= S[i]:
                break
            count += 1

        # Choose zero copies, and let the next call decide the next distinct value.
        self.helper(S, i + count, slate)
        # Append one additional copy per iteration to explore choices of 1 through count copies.
        for c in range(0,count):
            slate.append(S[i])
            self.helper(S,i+count,slate)

        for c in range(0,count):
            # Remove all copies added at this level to restore the caller's slate.
            slate.pop()



sol = Solution()
nums = [1,2,2]
print(sol.subsetsWithDup(nums))
