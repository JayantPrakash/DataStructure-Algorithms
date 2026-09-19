# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import List
# Group the state and operations used by the longest common prefix implementation.
class Solution:
    # Compute or update the longest common prefix result for the supplied input.
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Process each value from `range(len(strs[0]))`.
        for i in range(len(strs[0])):
            # Process each value from `strs`.
            for str in strs:
                # Choose this path when `i >= len(str) or strs[0][i] != str[i]` is true.
                if i >= len(str) or strs[0][i] != str[i]:
                    return str[:i]
        return strs[0]
strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
sol = Solution()

print(sol.longestCommonPrefix(strs))