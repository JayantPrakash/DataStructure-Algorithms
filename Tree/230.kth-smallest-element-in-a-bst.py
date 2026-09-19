# Key idea: Track the current node, the chosen subtree, and the value returned upward.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the kth smallest element in a bst implementation.
class Solution:
    # Compute or update the kth smallest result for the supplied input.
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes_val = []
        self.dfs(root)
        return self.nodes_val[k-1]

    # Traverse the reachable structure using DFS.
    def dfs(self, node):

        # Choose this path when `node.left is not None` is true.
        if node.left is not None:
            self.dfs(node.left)
        self.nodes_val.append(node.val)

        # Choose this path when `node.right is not None` is true.
        if node.right is not None:
            self.dfs(node.right)

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)     

print(sol.kthSmallest(root,3))                  
                