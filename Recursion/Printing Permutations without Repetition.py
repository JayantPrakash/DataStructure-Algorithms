# Key idea: Trace each recursive choice, the base case, and the backtracking step.
# Compute or update the ps helper result for the supplied input.
def ps_helper(slate, array):
    # Choose this path when `len(array) == 0` is true.
    if len(array) == 0:
        print(slate)
    else:
        # Process each value from `range(0, len(array) - 1)`.
        for i in range(0,len(array)-1):
            #ps_helper(slate + str(array[i]), str(array[:i]) + str(array[i+1,:]))
            ps_helper(slate + array[i], array[:i] + array[i+1:])

# Compute or update the permutation without rep result for the supplied input.
def permutation_without_rep(array):
    ps_helper(" ",array)

array = [1, 2, 3, 4,5]
#array = '123'
print(str(array[1:]))
permutation_without_rep(array)

#S(n) - O(n) - depth of stack - aux space
#T(n) = n + n(n-1) + n(n-1)(n-2) + ..1) = O(n!), to print = O(n!)*n
# here we keep array to keep track of which elem to chose