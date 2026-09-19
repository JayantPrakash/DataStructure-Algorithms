# Key idea: Track the current node, the chosen subtree, and the value returned upward.
# Group the state and operations used by the longest palindromic substring implementation.
class Solution:
    # Compute or update the longest palindrome result for the supplied input.
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        # Process each value from `range(len(s))`.
        for i in range(len(s)):
            l,r = i, i    

            # Keep processing while `l >= 0 and r < len(s) and (s[l] == s[r])` remains true.
            while l >=0 and r < len(s) and s[l] == s[r] :
                # Choose this path when `res_len < r - l + 1` is true.
                if res_len < r-l + 1:
                    res_len = r-l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

            l,r = i, i + 1   

            # Keep processing while `l >= 0 and r < len(s) and (s[l] == s[r])` remains true.
            while l >=0 and r < len(s) and s[l] == s[r] :
                # Choose this path when `res_len < r - l + 1` is true.
                if res_len < r-l + 1:
                    res_len = r-l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
                                
        return res

s = "babad"
sol = Solution()
print(sol.longestPalindrome(s))    