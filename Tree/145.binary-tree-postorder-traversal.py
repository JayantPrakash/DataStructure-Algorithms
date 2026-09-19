# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Postorder means left subtree, right subtree, then node: descendants finish before their parent.
    # O(n) time, O(h) recursive space, and O(n) output.
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postOrderHelper(root, result)
        return result
    
    def postOrderHelper(self,node, res):

        # Empty subtrees contribute nothing and terminate recursion safely.
        if not node:
            return None
        
        self.postOrderHelper(node.left, res)
        self.postOrderHelper(node.right, res)
        # Append only after both child calls return; moving this earlier would change traversal order.
        res.append(node.val)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.postorderTraversal(root))        

# Time and space complexity
# T(n) = O(n)
# S(n) = O(n)