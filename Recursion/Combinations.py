# Count k-element selections from n elements without regard to order; assumes 0 <= k <= n.
def combination(n,k):
    # There is exactly one way to choose nothing or choose every available element.
    if k == 0 or k == n:
        return 1
    else:
        # Split selections into those containing a distinguished element and those excluding it.
        # This is Pascal's recurrence; without memoization, repeated states cause exponential worst-case work.
        return combination(n-1,k-1) + combination(n-1,k)


print(combination(3,1))