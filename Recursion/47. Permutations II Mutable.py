# Key idea: Trace each recursive choice, the base case, and the backtracking step.
# Group the state and operations used by the Permutations II Mutable implementation.
class Solution(object):
    # Compute or update the permute result for the supplied input.
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.helper(nums,0,[])
        return self.result

    # Compute or update the helper result for the supplied input.
    def helper(self, S, i, slate):
        # Choose this path when `i == len(S)` is true.
        if i == len(S):
            self.result.append(slate[:])
            return
        else:
            hsmap = []
            # Process each value from `range(i, len(S))`.
            for pick in range(i,len(S)):
                # Choose this path when `S[pick] not in hsmap` is true.
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
