class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1 or len(s) % 2 != 0: return False
        dict = {")": "(", "}":"{", "]":"["}

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
                 
            else:
                if len(stack) > 0:
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
    