# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

# Group the state and operations used by the print all paths binary tree implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the print all paths binary tree implementation.
class Solution:
    # Compute or update the print all paths result for the supplied input.
    def print_all_paths(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Choose this path when `root is None` is true.
        if root is None:
            return []
        
        self.result = []

        self.dfs(root, [])
        return self.result

    # Traverse the reachable structure using DFS.
    def dfs(self, node, slate):

        slate.append(node.val)

        # Choose this path when `node.left is None and node.right is None` is true.
        if node.left is None and node.right is None:
            self.result.append(slate[:])

        # Choose this path when `node.left is not None` is true.
        if node.left is not None:
            self.dfs(node.left, slate)  

        # Choose this path when `node.right is not None` is true.
        if node.right is not None:
            self.dfs(node.right, slate)       

        slate.pop()           
    

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.print_all_paths(root))       