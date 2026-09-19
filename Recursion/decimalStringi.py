def decimal_string_i(n):
    ds_helper(n, '')


def ds_helper(n, slate):
    if n == 0:
        print(slate)
    else:
        for i in range(n):
            ds_helper(n - 1, slate + str(i))



(decimal_string_i(3))
#S(n) - O(n) - depth of tree - intermediate space
#T(n) - 0(10^n)
# Its a divide and conquer approach, every time manager will create 10 branches and it goes on.
# Its a permutation problem where repetition is allowed.