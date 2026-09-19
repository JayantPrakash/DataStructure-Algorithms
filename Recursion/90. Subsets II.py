# Key idea: Trace each recursive choice, the base case, and the backtracking step.
# Group the state and operations used by the Subsets II implementation.
class Solution(object):
    # Compute or update the subsets with dup result for the supplied input.
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums.sort()
        self.helper(nums,0,[])
        return self.result

    # Compute or update the helper result for the supplied input.
    def helper(self, S, i, slate):
        # Choose this path when `i == len(S)` is true.
        if i == len(S):
            self.result.append(slate[:])
            return
        count = 0
        # Process each value from `range(i, len(S))`.
        for index in range(i,len(S)):
            # Choose this path when `S[index] != S[i]` is true.
            if S[index]!= S[i]:
                break
            count += 1

        self.helper(S, i + count, slate)
        # manager will decide all the duplicate items of one type and pass them to subordinate,
        #subordinate will take decision on other items
        for c in range(0,count):
            slate.append(S[i])
            self.helper(S,i+count,slate)

        # Process each value from `range(0, count)`.
        for c in range(0,count):
            slate.pop()



sol = Solution()
nums = [1,2,2]
print(sol.subsetsWithDup(nums))

# space and time complexity will be same as subsets with mutable slate