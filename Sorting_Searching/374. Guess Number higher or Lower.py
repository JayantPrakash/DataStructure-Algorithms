import random
def guess(num,pick):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

def guessNumber(n,pick):
    start = 1
    end = n
    #if start == end:
    #    return 1
    while start <= end:
        mid = int(start + (end-start)/2)
        guess_result = guess(mid,pick)
        if guess_result == 0:
            return mid
        elif guess_result == 1:
            start = mid + 1
        else:
            end = mid - 1
    #return 1
#print(guessNumber(2126753390,1702766719))
print(guessNumber(10,1))

"""
edge case is when pick is 1, so always have guess(mid)== 0 at first in case statement
T(n) - O(logn)
S(n) - O(1)
"""