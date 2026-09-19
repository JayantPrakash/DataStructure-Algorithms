"""
Question:
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    # Normalize case and remove punctuation, then compare mirrored positions.
    # Creating cleaned_str makes this O(n) time and O(n) space, despite constant-space pointers.
    def isPalindrome(self, s: str) -> bool:

        cleaned_str = "".join(char.lower() for char in s if char.isalnum())
        
        l = 0
        r = len(cleaned_str) - 1

        # Each successful comparison rules out both ends; meeting in the middle proves symmetry.
        while l < r:
            # One mismatched mirrored pair is enough to reject the entire string.
            if cleaned_str[l] != cleaned_str[r]:
                return False
            
            l+=1
            r-=1

        # Empty and single-character cleaned strings are palindromes without any comparisons.
        return True
    

s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
sol = Solution()
print(sol.isPalindrome(s))