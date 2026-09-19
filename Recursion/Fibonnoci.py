# Key idea: Track how each state reuses results from smaller subproblems.
# Compute or update the fibonnoci result for the supplied input.
def fibonnoci(n):
    # Choose this path when `n == 0 or n == 1` is true.
    if n == 0 or n == 1:
        return n
    else:
        return fibonnoci(n-1) + fibonnoci(n-2)

print(fibonnoci(100))