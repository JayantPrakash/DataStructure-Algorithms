import random
# The oracle returns -1 for a guess too high, +1 for too low, and 0 for an exact match.
def guess(num,pick):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

# Maintain the inclusive candidate interval [start, end] and eliminate half after each oracle response.
# For a pick inside 1..n, O(log n) guesses and O(1) space suffice.
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
        # Exclude mid and all smaller candidates because the hidden pick is larger.
        elif guess_result == 1:
            start = mid + 1
        else:
            # A guess that is too high rules out mid and every larger candidate.
            end = mid - 1
    #return 1
#print(guessNumber(2126753390,1702766719))
print(guessNumber(10,1))

"""
edge case is when pick is 1, so always have guess(mid)== 0 at first in case statement
T(n) - O(logn)
S(n) - O(1)
"""