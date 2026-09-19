class Solution:
    # Keep the most common character in a window and replace all other characters.
    # Required replacements = window length - highest character frequency.
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        max_len = 0
        count = {}
        for R in range(len(s)):
            # Update counts when extending right so they describe the current substring.
            count[s[R]] = count.get(s[R],0) + 1

            # If replacements exceed k, remove left characters until the budget is satisfied.
            # max(count.values()) is recomputed: O(nu) time and O(u) space, or O(n) for a fixed alphabet.
            while (R-L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1

            # Only a budget-valid window contributes to the longest answer.
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