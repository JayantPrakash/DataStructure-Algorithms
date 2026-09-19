class Solution:
    # Sort and fix one element, then move two pointers through the remaining suffix.
    # The two-pointer search is O(n^2), but checking candidate membership in ans adds output-dependent work.
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # target is the fixed value, so look for a pair whose sum is its negation.
        def twoSum(l,r, target):

            while l < r:
                if nums[l] + nums[r] + target == 0:
                    candidate_3sum = [target,nums[l],nums[r]]
                    # Deduplicate by scanning previously found triples; this is costlier than skipping equal values.
                    if candidate_3sum not in ans:
                        ans.append(candidate_3sum)
                    l += 1    

                # Sorting makes pointer movement directional: move left up for a low sum, right down for a high sum.
                # Independent if statements re-evaluate the sum after earlier pointer moves.
                if nums[l] + nums[r] + target < 0:
                    l += 1
                if nums[l] + nums[r] + target > 0:
                    r -= 1

            return 
        
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            # A positive smallest element cannot form a zero-sum triple with later sorted elements.
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
