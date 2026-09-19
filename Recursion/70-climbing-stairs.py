class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2) 
    
sol = Solution()
print(sol.climbStairs(6))    

"""
T(n) = O(2^n)
S(n) = O(n)
"""