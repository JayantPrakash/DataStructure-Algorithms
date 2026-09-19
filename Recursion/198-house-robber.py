from typing import List
class Solution:
    # Let helper(i) be the best non-adjacent total among houses 0..i.
    # Memoization solves each prefix once: O(n) time and O(n) cache/recursion space.
    def rob(self, nums: List[int]) -> int:
        # Append a zero-valued dummy house to express the final answer as one recurrence call.
        # This mutates the caller's list; nonnegative house values are assumed.
        nums.append(0)
        mem = {}
        def helper(i: int )-> int:
            # Reuse a solved prefix instead of rebuilding the same recursion subtree.
            if i in mem:
                return mem[i]
            if i == 0:
                mem[i] = nums[0]
                return mem[i]
            # For the first two houses, choose one; taking both would violate non-adjacency.
            if i == 1:
                mem[i] = max(nums[0], nums[1]) 
                return mem[i] 
            # Either rob i and combine with prefix i-2, or skip i and keep prefix i-1.
            mem[i] = max(helper(i-2) + nums[i], helper(i-1))
            return mem[i]
        
        return helper(len(nums)-1)       

sol = Solution()
nums = [1,2,3,1]
nums = [2,7,9,3,1]
print(sol.rob(nums))    