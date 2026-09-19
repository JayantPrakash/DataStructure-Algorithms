# Key idea: Track how each state reuses results from smaller subproblems.
# Group the state and operations used by the fibonacci number implementation.
class Solution:
    # Compute or update the fib result for the supplied input.
    def fib(self, n: int) -> int:
        # Choose this path when `n == 0` is true.
        if n == 0:
            return 0
        # Choose this path when `n == 1` is true.
        if n == 1:
            return 1
        
        return self.fib(n-1) + self.fib(n-2) 


"""
T(n) = O(2^n)
S(n) = O(n)
"""        