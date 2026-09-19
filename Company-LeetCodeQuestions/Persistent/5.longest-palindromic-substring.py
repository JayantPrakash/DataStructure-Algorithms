class Solution:
    # Every palindrome has a center: one character for odd lengths, a gap for even lengths.
    # Expand all centers in O(n^2) comparisons, keeping the longest substring found.
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):
            # Odd-length center: the initial one-character interval is already symmetric.
            l,r = i, i    

            while l >=0 and r < len(s) and s[l] == s[r] :
                if res_len < r-l + 1:
                    res_len = r-l + 1
                    # Save the actual substring when the record grows; Python slicing allocates a new string.
                    res = s[l:r+1]
                # Matching endpoints allow testing the next larger symmetric interval.
                l -= 1
                r += 1

            # Even-length center: expansion starts only when the adjacent characters match.
            l,r = i, i + 1   

            while l >=0 and r < len(s) and s[l] == s[r] :
                if res_len < r-l + 1:
                    res_len = r-l + 1
                    # Save the actual substring when the record grows; Python slicing allocates a new string.
                    res = s[l:r+1]
                # Matching endpoints allow testing the next larger symmetric interval.
                l -= 1
                r += 1
                                
        return res

s = "babad"
sol = Solution()
print(sol.longestPalindrome(s))    