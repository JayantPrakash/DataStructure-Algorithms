# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import defaultdict
# Group the state and operations used by the group anagrams implementation.
class Solution(object):
    # Compute or update the group anagrams result for the supplied input.
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # it creates dict with empty list, 
        # not throw error in append
        res = defaultdict(list)

        # Process each value from `strs`.
        for s in strs:
            count = [0] * 26

            # Process each value from `s`.
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()        

strs = ["eat","tea","tan","ate","nat","bat"]   
sol = Solution()

print(sol.groupAnagrams(strs))

"""
from collections import defaultdict

d = defaultdict(list)

d["fruits"].append("apple")
d["fruits"].append("banana")

print(d)
defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})
"""