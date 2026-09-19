# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Enumerate root-to-leaf paths using one shared mutable path and depth-first traversal.
    # Work is O(n + P), where P is the total number of values copied into output paths.
    def print_all_paths(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None

        self.result = []
        self.slate = []
        self.dfs(root, self.slate)
        return self.result

    def dfs(self, node, slate):
        # Choose: include this node so the slate describes the full path from root to the current node.
        self.slate.append(node.val)

        # Only leaves finish a root-to-leaf path; an internal node with one missing child is not a leaf.
        if node.left is None and node.right is None:
            # Copy the path now; storing the shared list itself would let later backtracking change past answers.
            self.result.append(self.slate[:])

        if node.left is not None:
            self.dfs(node.left, slate)

        if node.right is not None:
            self.dfs(node.right, slate)

        # Unchoose: restore the parent's path before a sibling is explored.
        # The slate and recursion stack use O(h) auxiliary space for tree height h.
        self.slate.pop()

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)     
root.right.right = TreeNode(7)     

print(sol.print_all_paths(root))   