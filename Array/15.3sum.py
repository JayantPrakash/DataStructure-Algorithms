# Key idea: Track complements or pointer movement while avoiding repeated work.
# Group the state and operations used by the 3sum implementation.
class Solution:
    # Compute or update the three sum result for the supplied input.
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Compute or update the two sum result for the supplied input.
        def twoSum(l,r, target):

            # Keep processing while `l < r` remains true.
            while l < r:
                # Choose this path when `nums[l] + nums[r] + target == 0` is true.
                if nums[l] + nums[r] + target == 0:
                    candidate_3sum = [target,nums[l],nums[r]]
                    # Choose this path when `candidate_3sum not in ans` is true.
                    if candidate_3sum not in ans:
                        ans.append(candidate_3sum)
                    l += 1    

                # Choose this path when `nums[l] + nums[r] + target < 0` is true.
                if nums[l] + nums[r] + target < 0:
                    l += 1
                # Choose this path when `nums[l] + nums[r] + target > 0` is true.
                if nums[l] + nums[r] + target > 0:
                    r -= 1

            return 
        
        nums.sort()
        ans = []
        # Process each value from `range(len(nums) - 2)`.
        for i in range(len(nums) - 2):
            # Choose this path when `nums[i] > 0` is true.
            if nums[i] > 0:
                break
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            twoSum(left,right, target)
        return ans

sol = Solution()
nums = [-1,0,1,2,-1,-4]
nums = [0,1,1]
nums = [0,0,0]
print(sol.threeSum(nums))
