class Solution(object):
    # Build permutations of distinct values by fixing one position per recursion level.
    # Copying n! length-n answers costs O(n * n!) time/output space; active working space is O(n).
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.helper(nums,0,[])
        return self.result

    # S[:i] contains chosen positions; S[i:] contains values still available to pick.
    def helper(self, S, i, slate):
        if i == len(S):
            # At depth n the permutation is complete; copy the slate before it is reused.
            self.result.append(slate[:])
            return
        else:
            for pick in range(i,len(S)):
                # Choose a remaining value for position i by swapping it into the fixed prefix.
                S[i],S[pick] = S[pick], S[i]
                slate.append(S[i])
                self.helper(S,i+1,slate)
                # Undo both the slate append and the swap so the next sibling starts from the same state.
                slate.pop()
                S[i],S[pick] = S[pick], S[i]

sol = Solution()
nums = [1,2,3]
print(sol.permute(nums))

