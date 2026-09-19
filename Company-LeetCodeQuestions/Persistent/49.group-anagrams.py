from typing import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # it creates dict with empty list, 
        # not throw error in append
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

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