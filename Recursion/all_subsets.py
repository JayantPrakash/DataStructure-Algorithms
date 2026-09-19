# Key idea: Trace each recursive choice, the base case, and the backtracking step.
# Compute or update the subset hp result for the supplied input.
def subset_hp(slate, array):
    # Choose this path when `len(array) == 0` is true.
    if len(array) == 0:
        print(slate)
    else:
        subset_hp(slate, array[1:])
        subset_hp(slate + array[0], array[1:])


# Compute or update the all subsets result for the supplied input.
def all_subsets(array):
    subset_hp('', array)


array = '123'

all_subsets(array)

# S(n) - O(n)
# T(n) - 1 + 2 + 4 + 2^n = O(2^n) , printing - O(2^n) * n - n time for printing lenth of size n.
