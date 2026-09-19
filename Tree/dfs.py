# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
# Definition for a binary tree node.
from typing import List, Optional


# Group the state and operations used by the dfs implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the dfs implementation.
class Solution:
    # Traverse the reachable structure using DFS.
    def dfs(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        self.dfs_helper(root, result)
        return result
    
    # Compute or update the dfs helper result for the supplied input.
    def dfs_helper(self, node, res):
        
        # Choose this path when `node.left is not None` is true.
        if node.left is not None:
            self.dfs_helper(node.left, res)
        # Choose this path when `node.right is not None` is true.
        if node.right is not None:
            self.dfs_helper(node.right, res)

        res.append(node.val)

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
