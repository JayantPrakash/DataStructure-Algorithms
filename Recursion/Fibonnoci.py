# Fibonacci splits into the preceding two states, with F(0)=0 and F(1)=1.
# Without memoization, repeated subproblems give exponential time and O(n) recursion depth.
def fibonnoci(n):
    if n == 0 or n == 1:
        return n
    else:
        # The two branches overlap heavily (for example, both eventually recompute F(n-2)).
        # A cache or a bottom-up pair of running values would avoid that repetition.
        return fibonnoci(n-1) + fibonnoci(n-2)

print(fibonnoci(100))