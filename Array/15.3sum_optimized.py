from typing import List
class Solution:
    # Sort, fix one value, then solve two-sum on its suffix: O(n^2) scanning.
    # Sorting changes nums in place; skipping equal anchors and left values avoids duplicate triples.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Here target is the fixed first value; the other two must sum to -target.
        def twoSum(l,r, target):

            while l < r:
                if nums[l] + nums[r] + target == 0:
                    ans.append([target,nums[l],nums[r]])
                    l += 1  
                    r -= 1 
                    # After recording a triple, skip identical left values so it is not emitted again.
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
                # A negative total needs a larger left value; a positive total needs a smaller right value.
                # These are separate if statements, so later checks use any pointers already moved.
                if nums[l] + nums[r] + target < 0:
                    l += 1
                if nums[l] + nums[r] + target > 0:
                    r -= 1

            return 
        
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            # All remaining values are positive after sorting, so no later triple can sum to zero.
            if nums[i] > 0:
                break
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            # Only the first occurrence of each anchor needs its suffix searched.
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(left,right, target)
        return ans