# Intended state: slate is the chosen prefix; array contains unused values to choose next.
def ps_helper(slate, array):
    if len(array) == 0:
        print(slate)
    else:
        # This bound excludes the last candidate and produces no branch for a singleton remainder.
        # Consequently even string input never reaches a complete permutation through this loop.
        for i in range(0,len(array)-1):
            #ps_helper(slate + str(array[i]), str(array[:i]) + str(array[i+1,:]))
            # Removing the chosen element would prevent reuse, but the sample supplies integers.
            # Concatenating those integers to the string slate raises TypeError in this version.
            ps_helper(slate + array[i], array[:i] + array[i+1:])

# Start the recursive permutation experiment; the limitations above are retained in the code.
def permutation_without_rep(array):
    ps_helper(" ",array)

array = [1, 2, 3, 4,5]
#array = '123'
print(str(array[1:]))
permutation_without_rep(array)
