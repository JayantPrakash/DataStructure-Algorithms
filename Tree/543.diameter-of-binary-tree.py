# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the diameter of binary tree implementation.
class Solution:
    # Compute or update the diameter of binary tree result for the supplied input.
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.global_dia = 0

        self.dfs(root)

        return self.global_dia
    
    # Traverse the reachable structure using DFS.
    def dfs(self, node):

        # Choose this path when `node.left is None and node.right is None` is true.
        if node.left is None and node.right is None:
            return 0
        
        local_dia = 0
        left_dia = 0
        right_dia = 0

        # Choose this path when `node.left is not None` is true.
        if node.left is not None:
            left_dia = self.dfs(node.left)
            local_dia = left_dia + 1

        # Choose this path when `node.right is not None` is true.
        if node.right is not None:
            right_dia = self.dfs(node.right)
            local_dia += right_dia + 1

        # Choose this path when `self.global_dia < local_dia` is true.
        if self.global_dia < local_dia:
            self.global_dia = local_dia

        return max(left_dia, right_dia) + 1


            

