class Solution(object):
    # For lowercase a-z input, a fixed 26-entry frequency vector is a complete anagram signature.
    # O(n) time and O(1) auxiliary space because the alphabet size is fixed.
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Different string lengths immediately rule out identical multiplicities.
        if len(s) != len(t):
            return False

        dict_s, dict_t = {},{}
        count_s = [0]* 26
        count_t = [0] * 26

        for i in range(len(s)):
            # Map a-z to slots 0-25 and count both strings in the same pass.
            count_s[ord(s[i]) - ord("a")] +=  1
            count_t[ord(t[i]) - ord("a")] += 1


        # Vector equality checks every character count, including zero counts.
        return count_s == count_t

s = "anagram"
t = "nagaram"
#s = "rat"
#t = "car"
sol = Solution()
print(sol.isAnagram(s,t))

            