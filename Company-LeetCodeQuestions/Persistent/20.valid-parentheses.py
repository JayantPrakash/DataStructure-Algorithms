# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
# Group the state and operations used by the valid parentheses implementation.
class Solution:
    # Compute or update the is valid result for the supplied input.
    def isValid(self, s: str) -> bool:
        stack = []
        # Choose this path when `len(s) == 1 or len(s) % 2 != 0` is true.
        if len(s) == 1 or len(s) % 2 != 0: return False
        dict = {")": "(", "}":"{", "]":"["}

        # Process each value from `s`.
        for c in s:
            # Choose this path when `c == '(' or c == '{' or c == '['` is true.
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
                 
            else:
                # Choose this path when `len(stack) > 0` is true.
                if len(stack) > 0:
                    # Choose this path when `stack[-1] == dict[c]` is true.
                    if stack[-1] == dict[c]:
                        stack.pop(-1)
                    else:
                        return False  
                else:
                    return False             

        return len(stack) == 0

s = "()"
s = "()[]{}"
s = "(]"
s = "([])"
s = "([)]"
s = "[({(())}[()])]"
sol = Solution()
print(sol.isValid(s))
    