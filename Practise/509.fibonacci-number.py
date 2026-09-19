class Solution:
    # Fibonacci splits into the preceding two states, with F(0)=0 and F(1)=1.
    # Without memoization, repeated subproblems give exponential time and O(n) recursion depth.
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # The two branches overlap heavily (for example, both eventually recompute F(n-2)).
        # A cache or a bottom-up pair of running values would avoid that repetition.
        return self.fib(n-1) + self.fib(n-2) 


"""
T(n) = O(2^n)
S(n) = O(n)
"""        