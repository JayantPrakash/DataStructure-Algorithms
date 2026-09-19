from typing import List
class Solution:
    # Two pointers start at maximum width; each step discards a boundary that cannot improve the answer.
    # O(n) time and O(1) auxiliary space.
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            # The shorter wall limits the water level; width is the distance between indices.
            length = min(height[l], height[r])
            breadth = r - l
            local_area = length * breadth
            max_area =  max(max_area, local_area)
            # Keeping the shorter wall while shrinking width cannot help, so move that wall inward.
            # A taller replacement is the only chance to compensate for the smaller width.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1     

        return max_area

sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
print(sol.maxArea(height))
