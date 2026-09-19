def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))

# T(n) = O(2^n) as every node will make 2 calls. 
#S(n) = O(n) as we are using stack space
