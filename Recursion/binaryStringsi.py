# Build length-n strings from the full collection of length-(n-1) strings; assumes n >= 1.
def binaryStringsi(n):
    # The two one-bit strings seed the recursive construction; there is no base case for n == 0.
    if n == 1:
        return ['0','1']
    else:
        prev = binaryStringsi(n-1)
        result = []
        # Each shorter string has exactly two extensions, so the result doubles at each level.
        for elem in prev:
            result.append(elem + '0')
            result.append(elem + '1')
        # Storing 2^n strings of length n requires O(n * 2^n) space and character-copying time.
        return result

print(binaryStringsi(3))

