# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
# Definition for a binary tree node.
from typing import List, Optional

# Group the state and operations used by the binary tree postorder traversal implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the binary tree postorder traversal implementation.
class Solution:
    # Compute or update the postorder traversal result for the supplied input.
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postOrderHelper(root, result)
        return result
    
    # Compute or update the post order helper result for the supplied input.
    def postOrderHelper(self,node, res):

        # Choose this path when `not node` is true.
        if not node:
            return None
        
        self.postOrderHelper(node.left, res)
        self.postOrderHelper(node.right, res)
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