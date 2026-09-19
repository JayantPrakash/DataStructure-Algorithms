from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        mem = {}
        def helper(i: int )-> int:
            if i in mem:
                return mem[i]
            if i == 0:
                mem[i] = nums[0]
                return mem[i]
            if i == 1:
                mem[i] = max(nums[0], nums[1]) 
                return mem[i] 
            mem[i] = max(helper(i-2) + nums[i], helper(i-1))
            return mem[i]
        
        return helper(len(nums)-1)       

sol = Solution()
nums = [1,2,3,1]
nums = [2,7,9,3,1]
print(sol.rob(nums))    