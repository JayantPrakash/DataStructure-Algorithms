# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
# Group the state and operations used by the valid anagram implementation.
class Solution(object):
    # Compute or update the is anagram result for the supplied input.
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Choose this path when `len(s) != len(t)` is true.
        if len(s) != len(t):
            return False

        dict_s, dict_t = {},{}
        count_s = [0]* 26
        count_t = [0] * 26

        # Process each value from `range(len(s))`.
        for i in range(len(s)):
            count_s[ord(s[i]) - ord("a")] +=  1
            count_t[ord(t[i]) - ord("a")] += 1


        return count_s == count_t

s = "anagram"
t = "nagaram"
#s = "rat"
#t = "car"
sol = Solution()
print(sol.isAnagram(s,t))

            