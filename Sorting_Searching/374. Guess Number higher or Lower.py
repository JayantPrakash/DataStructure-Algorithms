# Key idea: Track how values move toward their final sorted positions.
import random
# Compute or update the guess result for the supplied input.
def guess(num,pick):
    # Choose this path when `num > pick` is true.
    if num > pick:
        return -1
    # Choose this path when `num < pick` is true.
    elif num < pick:
        return 1
    else:
        return 0

# Compute or update the guess number result for the supplied input.
def guessNumber(n,pick):
    start = 1
    end = n
    #if start == end:
    #    return 1
    while start <= end:
        mid = int(start + (end-start)/2)
        guess_result = guess(mid,pick)
        # Choose this path when `guess_result == 0` is true.
        if guess_result == 0:
            return mid
        # Choose this path when `guess_result == 1` is true.
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