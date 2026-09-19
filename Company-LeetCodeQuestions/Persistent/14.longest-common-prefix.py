from typing import List
class Solution:
    # Compare strings vertically: column i belongs to the prefix only if every string matches it.
    # Assumes at least one string; O(mk) comparisons for m strings and k checked columns.
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for str in strs:
                # A shorter string or first mismatch ends the shared prefix; all earlier columns already matched.
                if i >= len(str) or strs[0][i] != str[i]:
                    return str[:i]
        # If every column of the first string matched, that entire string is the common prefix.
        return strs[0]
strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
sol = Solution()

print(sol.longestCommonPrefix(strs))