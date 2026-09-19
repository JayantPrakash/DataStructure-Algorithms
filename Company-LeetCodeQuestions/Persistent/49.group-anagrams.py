from typing import defaultdict
class Solution(object):
    # For lowercase a-z words, character counts identify anagrams regardless of letter order.
    # Counting all characters is linear in input size; each word is placed into one signature bucket.
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # A missing signature automatically gets an empty list, allowing its first word to be appended directly.
        res = defaultdict(list)

        for s in strs:
            # Use a fresh 26-slot signature for each word; repeated letters must contribute repeatedly.
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            # Convert the mutable list to a hashable tuple so identical signatures share one dictionary key.
            res[tuple(count)].append(s)

        # Return the grouped buckets as a dictionary-values view.
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