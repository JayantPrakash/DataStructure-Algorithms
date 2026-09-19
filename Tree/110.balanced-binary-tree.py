# Key idea: Track the current node, the chosen subtree, and the value returned upward.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the balanced binary tree implementation.
class Solution:
    # Compute or update the is balanced result for the supplied input.
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Choose this path when `root is None` is true.
        if root is None:
            return True
        self.isBalanced = True
        self.dfs(root)
        return self.isBalanced
    
    # Traverse the reachable structure using DFS.
    def dfs(self, node):

        # Choose this path when `node.left is None and node.right is None` is true.
        if node.left is None and node.right is None:
            return 1
        
        left_depth = 0
        right_depth = 0

        # Choose this path when `node.left is not None` is true.
        if node.left is not None:
            left_depth = self.dfs(node.left)

        # Choose this path when `node.right is not None` is true.
        if node.right is not None:
            right_depth = self.dfs(node.right)

        # Choose this path when `abs(left_depth - right_depth) > 1` is true.
        if abs(left_depth - right_depth) > 1:
            self.isBalanced = False

        return max(left_depth, right_depth) + 1


            
"""
Make sure to have the depth of leaf node to be 1,
otherwise only node with right subtree will give wrong result
ex: [1,null,2,null,3]

"""
