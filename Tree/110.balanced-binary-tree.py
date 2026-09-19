from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # A tree is height-balanced only if every node's subtree heights differ by at most one.
    # Postorder computes each height once: O(n) time and O(h) stack space.
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        # This instance attribute shadows the method with a boolean; a second call on the same instance is not callable.
        self.isBalanced = True
        self.dfs(root)
        return self.isBalanced
    
    # Return subtree height in nodes: a leaf has height 1 and a missing child contributes 0.
    def dfs(self, node):

        if node.left is None and node.right is None:
            return 1
        
        # Default heights represent absent children; recurse only into children that exist.
        left_depth = 0
        right_depth = 0

        if node.left is not None:
            left_depth = self.dfs(node.left)

        if node.right is not None:
            right_depth = self.dfs(node.right)

        # The local balance check uses both completed child heights; any failure makes the shared answer false.
        if abs(left_depth - right_depth) > 1:
            self.isBalanced = False

        # Return height, not balance: the parent needs the longest downward branch plus this node.
        return max(left_depth, right_depth) + 1


            
"""
Make sure to have the depth of leaf node to be 1,
otherwise only node with right subtree will give wrong result
ex: [1,null,2,null,3]

"""
