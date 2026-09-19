from typing import List
class Solution:
    # Keep only earlier values whose indices are at most k positions from R.
    # Expected O(n) time and O(min(n, k + 1)) space for nonnegative k.
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            # Expire an index before checking the new value, otherwise a distant duplicate could match.
            if R - L > k:
                window.remove(nums[L])
                L += 1

            # A match is now both equal in value and close enough in index.
            # The set is sufficient: any duplicate still inside the window would already have returned True.
            if nums[R] in window:
                return True

            window.add(nums[R])

        return False

sol = Solution()
nums = [1,2,3,1]
k = 3

nums = [1,0,1,1]
k = 1

nums = [1,2,3,1,2,3]
k = 2
print(sol.containsNearbyDuplicate(nums,k))            