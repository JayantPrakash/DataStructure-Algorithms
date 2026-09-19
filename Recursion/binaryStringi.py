# Enumerate all length-n binary strings by making two choices at each position.
def binary_string_i(n):
    bs_helper(n, '')


# n is the number of positions left; slate is the prefix already chosen.
def bs_helper(n, slate):
    # A complete prefix is a leaf; print it only after every position is assigned.
    if n == 0:
        print(slate)
    else:
        # Explore both possible next bits. Immutable strings need no explicit backtracking.
        # There are 2^n outputs of length n; printing takes O(n * 2^n), with O(n^2) retained prefix characters on a deep chain.
        bs_helper(n - 1, slate + '0')
        bs_helper(n - 1, slate + '1')


(binary_string_i(3))