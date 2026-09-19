class Solution(object):
    # Generate distinct permutations when values repeat; duplicate choices must be suppressed at each depth.
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
            # Save a copy only when every position is fixed; subsequent backtracking mutates the live slate.
            self.result.append(slate[:])
            return
        else:
            # This per-call list remembers values already placed at position i, not values used globally.
            hsmap = []
            for pick in range(i,len(S)):
                # Choosing an equal value again at the same depth would recreate the same suffix permutations.
                # Membership here is linear because hsmap is a list.
                if S[pick] not in hsmap:
                    #continue
                    S[i],S[pick] = S[pick], S[i]
                    slate.append(S[i])
                    self.helper(S,i+1,slate)
                    # Restore slate and swapped input before recording the tried value and trying another choice.
                    slate.pop()
                    S[i],S[pick] = S[pick], S[i]
                    hsmap.append(S[pick])


sol = Solution()
nums = [2,2,1,1]
print(sol.permute(nums))
