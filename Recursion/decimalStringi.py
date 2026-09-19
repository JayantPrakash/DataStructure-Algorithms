# Despite the name, this code does not enumerate all base-10 strings: branch choices shrink with n.
def decimal_string_i(n):
    ds_helper(n, '')


# slate is the chosen prefix and n is the remaining recursion depth.
def ds_helper(n, slate):
    # Print when all decisions are made; concatenated str(i) may occupy several characters when i >= 10.
    if n == 0:
        print(slate)
    else:
        # Choose from 0..n-1 here, then only 0..n-2 below: n! leaves rather than 10^n.
        # For initial n == 3 the available symbols per position are {0,1,2}, then {0,1}, then {0}.
        for i in range(n):
            ds_helper(n - 1, slate + str(i))



(decimal_string_i(3))