def fibonnoci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonnoci(n-1) + fibonnoci(n-2)

print(fibonnoci(100))