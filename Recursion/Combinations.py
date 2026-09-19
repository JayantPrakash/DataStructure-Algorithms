def combination(n,k):
    if k == 0 or k == n:
        return 1
    else:
        return combination(n-1,k-1) + combination(n-1,k)


print(combination(3,1))