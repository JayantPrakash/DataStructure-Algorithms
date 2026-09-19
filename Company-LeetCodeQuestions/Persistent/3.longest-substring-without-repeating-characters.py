import math
class Solution:
    def lengthOfLongestSubstring(self, s):
        L = 0
        len_longest_char = -math.inf
        window = set()
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1

            window.add(s[R])
            if len(window) > len_longest_char:
                len_longest_char = len(window)
                
        return len_longest_char

s = "abcabcbb"
#s = "pwwkew"
s = "bbbbb"
s = "1R1T7"

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
    
        