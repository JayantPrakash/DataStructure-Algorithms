# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import List
# Group the state and operations used by the container with most water implementation.
class Solution:
    # Compute or update the max area result for the supplied input.
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        # Keep processing while `l < r` remains true.
        while l < r:
            length = min(height[l], height[r])
            breadth = r - l
            local_area = length * breadth
            max_area =  max(max_area, local_area)
            # Choose this path when `height[l] < height[r]` is true.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1     

        return max_area

sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
print(sol.maxArea(height))
