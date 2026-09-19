# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
# Group the state and operations used by the valid anagram implementation.
class Solution:
    # Compute or update the is anagram result for the supplied input.
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}

        # Choose this path when `len(s) != len(t)` is true.
        if len(s) != len(t): return False
        
        # Process each value from `list(s)`.
        for key in list(s):
            # Choose this path when `key not in s_dict.keys()` is true.
            if key not in s_dict.keys():
                s_dict[key] = 1
            else:
                  s_dict[key] = s_dict[key] + 1

        # Process each value from `list(t)`.
        for key in list(t):
            # Choose this path when `key not in t_dict.keys()` is true.
            if key not in t_dict.keys():
                t_dict[key] = 1
            else:
                  t_dict[key] = t_dict[key] + 1

        # Process each value from `s_dict.items()`.
        for k, v in s_dict.items():
             
             # Choose this path when `k not in t_dict.keys() or s_dict[k] != t_dict[k]` is true.
             if k not in t_dict.keys() or s_dict[k] != t_dict[k]:
                  return False

        return True     





        return True    

sol = Solution()
print(sol.isAnagram( s = "anagram", t = "nagaram"))
print(sol.isAnagram(s = "rat", t = "car"))