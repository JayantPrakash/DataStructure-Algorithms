def binary_string_i(n):
    bs_helper(n, '')


def bs_helper(n, slate):
    if n == 0:
        print(slate)
    else:
        bs_helper(n - 1, slate + '0')
        bs_helper(n - 1, slate + '1')


(binary_string_i(3))
#S(n) - O(n) - depth of tree
#T(n) - 0(2^n)
# Its a divide and conquer approach, every time manager will create 2 branches and it goes on.
# Its a permutation problem where repetition is allowed.