from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Mirror the tree by swapping left and right references at every node in place.
    # O(n) time and O(h) recursion space; the returned root is the same object.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        self.root = root
        self.dfs(self.root)
        return self.root


    # This version is postorder: fully invert both original subtrees before swapping their positions.
    def dfs(self,node):

        if node.left is not None:
            self.dfs(node.left)

        if node.right is not None:
            self.dfs(node.right)

        # Preserve the original left reference while replacing it, then attach it as the new right subtree.
        temp_node = node.left
        node.left = node.right
        node.right = temp_node        