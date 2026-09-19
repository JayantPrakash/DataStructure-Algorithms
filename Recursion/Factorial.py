# Reduce n! to n times (n-1)!; assumes a nonnegative integer.
def factorial(n):
    # 0! is the empty product, equal to 1, and stops the recursive descent.
    if n == 0:
        return 1
    else:
        # Multiplications happen while calls return; O(n) recursive calls and O(n) stack depth.
        # For large n, integer multiplication costs and Python's recursion limit also matter.
        return n * factorial(n-1)


print(factorial(100))