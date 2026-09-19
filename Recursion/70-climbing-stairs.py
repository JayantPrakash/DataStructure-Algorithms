class Solution:
    # Partition paths by their last jump: reaching n comes from n-1 by one step or n-2 by two steps.
    # Without memoization the repeated subproblems take exponential time and O(n) stack space.
    def climbStairs(self, n: int) -> int:
        # For the positive-n problem, one step has one route and two steps have two routes.
        # This implementation returns zero for n == 0 rather than counting an empty route.
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2) 
    
sol = Solution()
print(sol.climbStairs(6))    

"""
T(n) = O(2^n)
S(n) = O(n)
"""