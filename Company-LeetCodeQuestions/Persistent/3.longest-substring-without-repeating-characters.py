# Key idea: Track the current node, the chosen subtree, and the value returned upward.
import math
# Group the state and operations used by the longest substring without repeating characters implementation.
class Solution:
    # Compute or update the length of longest substring result for the supplied input.
    def lengthOfLongestSubstring(self, s):
        L = 0
        len_longest_char = -math.inf
        window = set()
        # Process each value from `range(len(s))`.
        for R in range(len(s)):
            # Keep processing while `s[R] in window` remains true.
            while s[R] in window:
                window.remove(s[L])
                L += 1

            window.add(s[R])
            # Choose this path when `len(window) > len_longest_char` is true.
            if len(window) > len_longest_char:
                len_longest_char = len(window)
                
        return len_longest_char

s = "abcabcbb"
#s = "pwwkew"
s = "bbbbb"
s = "1R1T7"

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
    
        