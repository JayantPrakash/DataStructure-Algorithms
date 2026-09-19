# Key idea: Track the current node, the chosen subtree, and the value returned upward.
# Group the state and operations used by the longest substring without repeating characters implementation.
class Solution:
    # Compute or update the length of longest substring result for the supplied input.
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        max_len = 0

        # Process each value from `range(len(s))`.
        for R in range(len(s)):
            # Keep processing while `s[R] in window` remains true.
            while s[R] in window:
                window.remove(s[L])
                L += 1

            window.add(s[R]) 
            max_len = max(len(window), max_len)

        return max_len        
    

sol = Solution()
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
s = "1R1T7"
print(sol.lengthOfLongestSubstring(s))    