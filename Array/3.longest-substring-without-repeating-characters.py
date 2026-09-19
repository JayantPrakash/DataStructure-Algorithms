class Solution:
    # Maintain a contiguous window containing no repeated characters.
    # Each character enters and leaves the set at most once: expected O(n) time and O(u) space.
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        max_len = 0

        for R in range(len(s)):
            # Remove from the left until the earlier copy of s[R] is gone; one removal may not be enough.
            while s[R] in window:
                window.remove(s[L])
                L += 1

            # After repairing uniqueness, include s[R]; the set size now equals the substring length.
            window.add(s[R]) 
            max_len = max(len(window), max_len)

        return max_len        
    

sol = Solution()
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
s = "1R1T7"
print(sol.lengthOfLongestSubstring(s))    