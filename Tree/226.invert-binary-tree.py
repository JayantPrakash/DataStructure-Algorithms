# Key idea: Track the current node, the chosen subtree, and the value returned upward.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the invert binary tree implementation.
class Solution:
    # Compute or update the invert tree result for the supplied input.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Choose this path when `root is None` is true.
        if root is None:
            return None
        
        self.root = root
        self.dfs(self.root)
        return self.root


    # Traverse the reachable structure using DFS.
    def dfs(self,node):

        # Choose this path when `node.left is not None` is true.
        if node.left is not None:
            self.dfs(node.left)

        # Choose this path when `node.right is not None` is true.
        if node.right is not None:
            self.dfs(node.right)

        temp_node = node.left
        node.left = node.right
        node.right = temp_node        