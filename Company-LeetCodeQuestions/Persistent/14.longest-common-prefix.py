from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for str in strs:
                if i >= len(str) or strs[0][i] != str[i]:
                    return str[:i]
        return strs[0]
strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
sol = Solution()

print(sol.longestCommonPrefix(strs))