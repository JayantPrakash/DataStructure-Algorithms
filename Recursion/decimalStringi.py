# Key idea: Trace each recursive choice, the base case, and the backtracking step.
# Compute or update the decimal string i result for the supplied input.
def decimal_string_i(n):
    ds_helper(n, '')


# Compute or update the ds helper result for the supplied input.
def ds_helper(n, slate):
    # Choose this path when `n == 0` is true.
    if n == 0:
        print(slate)
    else:
        # Process each value from `range(n)`.
        for i in range(n):
            ds_helper(n - 1, slate + str(i))



(decimal_string_i(3))
#S(n) - O(n) - depth of tree - intermediate space
#T(n) - 0(10^n)
# Its a divide and conquer approach, every time manager will create 10 branches and it goes on.
# Its a permutation problem where repetition is allowed.