# Key idea: Trace each recursive choice, the base case, and the backtracking step.
# Compute or update the combination result for the supplied input.
def combination(n,k):
    # Choose this path when `k == 0 or k == n` is true.
    if k == 0 or k == n:
        return 1
    else:
        return combination(n-1,k-1) + combination(n-1,k)


print(combination(3,1))