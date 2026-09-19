# Key idea: Trace each recursive choice, the base case, and the backtracking step.
# Compute or update the binary stringsi result for the supplied input.
def binaryStringsi(n):
    # Choose this path when `n == 1` is true.
    if n == 1:
        return ['0','1']
    else:
        prev = binaryStringsi(n-1)
        result = []
        # Process each value from `prev`.
        for elem in prev:
            result.append(elem + '0')
            result.append(elem + '1')
        return result

print(binaryStringsi(3))

#Here bs(3) - bs(2) - bs(1) - bs(0) will be called if n =3. At the last, bs(n), there will be 2^n-1 elements of length n-1 and
#then 0 and 1 will be added. Hence manager at the last will do the 2^n work.

#S(n) - O(2^n) - last call will 2^n-1 elements
#T(n) - O(2^n) , when printing O(2^n)*n - 1 + 2 + 4 + ..+2^n - there are 2 append for each elem.
# Its a decrease and conquer approach at the right side, the nth manager will take the output from n-1 child and append 0 or 1 to
# every element of child work.
# Its a permutation problem where repetition is allowed.