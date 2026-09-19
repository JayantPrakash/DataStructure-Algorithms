# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
# Group the state and operations used by the longest repeating character replacement implementation.
class Solution:
    # Compute or update the character replacement result for the supplied input.
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        max_len = 0
        count = {}
        # Process each value from `range(len(s))`.
        for R in range(len(s)):
            count[s[R]] = count.get(s[R],0) + 1

            # Keep processing while `R - L + 1 - max(count.values()) > k` remains true.
            while (R-L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1

            max_len = max(R-L+1, max_len)    
        return max_len

sol = Solution()
s = "ABAB"
k = 2
print(sol.characterReplacement(s,k))       


"""
T(n) = O(nm)
S(n) = O(m)
"""