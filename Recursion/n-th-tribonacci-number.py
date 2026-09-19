class Solution:
    # Use T(n) = T(n-1) + T(n-2) + T(n-3), with seeds 0, 1, 1 for nonnegative n.
    def tribonacci(self, n: int) -> int:
        if n <=1:
            return n
        # This third seed prevents recursion from falling into negative indices.
        if n == 2:
            return 1
        
        # Repeated states are recomputed without caching: exponential time (O(3^n) upper bound), O(n) stack depth.
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)   
    
    
sol = Solution()
print(sol.tribonacci(4))     