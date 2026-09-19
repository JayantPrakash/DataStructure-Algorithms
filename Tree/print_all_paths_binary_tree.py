# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Enumerate root-to-leaf paths with one shared slate and backtracking.
    # O(n + P) time for n visits plus P copied output values; O(h) working space.
    def print_all_paths(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        self.result = []

        self.dfs(root, [])
        return self.result

    def dfs(self, node, slate):

        # Choose: extend the root-to-parent path with this node.
        slate.append(node.val)

        # Only a node with no children completes a root-to-leaf path.
        if node.left is None and node.right is None:
            # Snapshot the path; appending the shared slate itself would let later mutations corrupt saved answers.
            self.result.append(slate[:])

        if node.left is not None:
            self.dfs(node.left, slate)  

        if node.right is not None:
            self.dfs(node.right, slate)       

        # Unchoose after both children to restore the caller's path before it explores a sibling.
        slate.pop()           
    

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.print_all_paths(root))       