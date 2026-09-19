# Key idea: Track the current node, the chosen subtree, and the value returned upward.
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode(object):
     # Initialize the state needed by a new instance.
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the binary tree longest consecutive sequence implementation.
class Solution(object):
    # Compute or update the longest consecutive result for the supplied input.
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.max_len = 1
        self.dfs(root, 1)
        
        return self.max_len
    
    # Traverse the reachable structure using DFS.
    def dfs(self, node, curr_len):

        # Choose this path when `node.left is not None` is true.
        if node.left is not None:
            # Choose this path when `node.left.val - node.val == 1` is true.
            if node.left.val - node.val == 1:
                self.dfs(node.left, curr_len+1)
            else:
                self.dfs(node.left, 1)
    
        # Choose this path when `node.right is not None` is true.
        if node.right is not None:
            # Choose this path when `node.right.val - node.val == 1` is true.
            if node.right.val - node.val == 1:
                self.dfs(node.right, curr_len+1)
            else:
                self.dfs(node.right, 1)

        # Choose this path when `curr_len > self.max_len` is true.
        if curr_len > self.max_len:
            self.max_len = curr_len
                


    
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
#root.left.left = TreeNode(3)
#root.left.right = TreeNode(5)
#root.right.right = TreeNode(6)     

print(sol.longestConsecutive(root))  