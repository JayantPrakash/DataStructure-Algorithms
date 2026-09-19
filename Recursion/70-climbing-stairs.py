# Key idea: Track how each state reuses results from smaller subproblems.
# Group the state and operations used by the climbing stairs implementation.
class Solution:
    # Compute or update the climb stairs result for the supplied input.
    def climbStairs(self, n: int) -> int:
        # Choose this path when `n <= 2` is true.
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2) 
    
sol = Solution()
print(sol.climbStairs(6))    

"""
T(n) = O(2^n)
S(n) = O(n)
"""