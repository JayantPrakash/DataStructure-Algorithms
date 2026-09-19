# Key idea: Track how each state reuses results from smaller subproblems.
# Compute or update the fibonacci result for the supplied input.
def fibonacci(n):
    # Choose this path when `n <= 1` is true.
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))

# T(n) = O(2^n) as every node will make 2 calls. 
#S(n) = O(n) as we are using stack space
