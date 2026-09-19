class Solution(object):
    #def __init__(self):
    #    self.result = []

    # For each input value choose exclude or include, giving 2^n subsets when values are distinct.
    # Copying answers costs O(n * 2^n) time/output space; the active slate and stack use O(n).
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []

        self.helper(nums, 0, [])
        return self.result

    # i is the next undecided input position; slate contains only choices from earlier positions.
    def helper(self, S, i, slate):
        if i == len(S):
            # Save a snapshot at a leaf; without copying, every result would reference the same mutable list.
            self.result.append(slate[:])
            return
        else:
            # First explore exclusion; then append S[i] and explore inclusion.
            self.helper(S, i + 1, slate)
            slate.append(S[i])
            self.helper(S, i + 1, slate)
            # Restore the slate to the caller's state so one branch cannot leak choices into another.
            slate.pop()


nums = [1, 2, 3]

sol = Solution()
print(sol.subsets(nums))



