class Solution:
    # A stack tracks unmatched opening brackets; closing brackets must match the most recent opener.
    # This enforces nesting, not just equal counts; O(n) time and O(n) space.
    def isValid(self, s: str) -> bool:
        stack = []
        # A balanced bracket-only string has pairs, so an odd length is impossible.
        if len(s) == 1 or len(s) % 2 != 0: return False
        dict = {")": "(", "}":"{", "]":"["}

        for c in s:
            # An opener postpones validation until its matching closer arrives.
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
                 
            else:
                if len(stack) > 0:
                    # Only the top may close next; a mismatch or an empty stack makes the nesting invalid.
                    if stack[-1] == dict[c]:
                        stack.pop(-1)
                    else:
                        return False  
                else:
                    return False             

        # All openings must have been closed; leftover entries represent incomplete pairs.
        return len(stack) == 0

s = "()"
s = "()[]{}"
s = "(]"
s = "([])"
s = "([)]"
s = "[({(())}[()])]"
sol = Solution()
print(sol.isValid(s))
    