import math
class Solution:
    # Slide a unique-character window; each boundary moves forward at most n times.
    # Expected O(n) time and O(u) space. This version returns -inf for empty input.
    def lengthOfLongestSubstring(self, s):
        L = 0
        len_longest_char = -math.inf
        window = set()
        for R in range(len(s)):
            # Evict characters from the left until the previous occurrence of the incoming character is removed.
            while s[R] in window:
                window.remove(s[L])
                L += 1

            window.add(s[R])
            # With uniqueness restored, set size equals the length of the contiguous window.
            if len(window) > len_longest_char:
                len_longest_char = len(window)
                
        return len_longest_char

s = "abcabcbb"
#s = "pwwkew"
s = "bbbbb"
s = "1R1T7"

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
    
        