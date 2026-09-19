class Solution:
    # Anagrams must have identical character multiplicities, not just the same distinct characters.
    # Two frequency maps give expected O(n) time and O(u) space for u distinct characters.
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}

        # Different lengths cannot be permutations of the same characters.
        if len(s) != len(t): return False
        
        # Count the first string; the second loop independently builds the comparison counts.
        for key in list(s):
            if key not in s_dict.keys():
                s_dict[key] = 1
            else:
                  s_dict[key] = s_dict[key] + 1

        for key in list(t):
            if key not in t_dict.keys():
                t_dict[key] = 1
            else:
                  t_dict[key] = t_dict[key] + 1

        # Equal total lengths plus equal counts for every character in s rule out extra characters in t.
        for k, v in s_dict.items():
             
             if k not in t_dict.keys() or s_dict[k] != t_dict[k]:
                  return False

        return True     





        return True    

sol = Solution()
print(sol.isAnagram( s = "anagram", t = "nagaram"))
print(sol.isAnagram(s = "rat", t = "car"))