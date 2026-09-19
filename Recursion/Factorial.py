# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
# Compute or update the factorial result for the supplied input.
def factorial(n):
    # Choose this path when `n == 0` is true.
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(100))