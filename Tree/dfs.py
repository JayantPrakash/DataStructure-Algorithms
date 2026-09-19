# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # This DFS returns postorder values: left subtree, right subtree, then parent.
    # O(n) time, O(h) recursion space, and O(n) output; empty input returns None here.
    def dfs(self, root: Optional[TreeNode]) -> List[int]:
        if root is None : return None
        self.result = []
        self.dfs_helper(root)
        return self.result
    
    # Each call finishes both child branches before contributing the current node.
    def dfs_helper(self, node):
        
        if node.left is not None:
            self.dfs_helper(node.left)
        if node.right is not None:
            self.dfs_helper(node.right)

        # The append occurs after both recursive calls, which is what makes this postorder.
        self.result.append(node.val)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.dfs(root))

# Time and space complexity
# T(n) = O(n)
# S(n) = O(n)
