# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
# Definition for a binary tree node.
from typing import List, Optional

# Group the state and operations used by the binary tree inorder traversal implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the binary tree inorder traversal implementation.
class Solution:
    # Compute or update the inorder traversal result for the supplied input.
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inOrderHelper(root, result)
        return result
    
    # Compute or update the in order helper result for the supplied input.
    def inOrderHelper(self,node, res):

        # Choose this path when `not node` is true.
        if not node:
            return None
        
        self.inOrderHelper(node.left, res)
        res.append(node.val)
        self.inOrderHelper(node.right, res)


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.inorderTraversal(root))        

# Time and space complexity
# T(n) = O(n)
# S(n) = O(n)