# Key idea: Track the active range and the condition that moves its boundaries.
"""
Question:
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

# Group the state and operations used by the valid palindrome implementation.
class Solution:
    # Compute or update the is palindrome result for the supplied input.
    def isPalindrome(self, s: str) -> bool:

        cleaned_str = "".join(char.lower() for char in s if char.isalnum())
        
        l = 0
        r = len(cleaned_str) - 1

        # Keep processing while `l < r` remains true.
        while l < r:
            # Choose this path when `cleaned_str[l] != cleaned_str[r]` is true.
            if cleaned_str[l] != cleaned_str[r]:
                return False
            
            l+=1
            r-=1

        return True
    

s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
sol = Solution()
print(sol.isPalindrome(s))