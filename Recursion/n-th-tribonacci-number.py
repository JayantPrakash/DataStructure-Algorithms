# Key idea: Track how each state reuses results from smaller subproblems.
# Group the state and operations used by the n th tribonacci number implementation.
class Solution:
    # Compute or update the tribonacci result for the supplied input.
    def tribonacci(self, n: int) -> int:
        # Choose this path when `n <= 1` is true.
        if n <=1:
            return n
        # Choose this path when `n == 2` is true.
        if n == 2:
            return 1
        
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)   
    
    
sol = Solution()
print(sol.tribonacci(4))     