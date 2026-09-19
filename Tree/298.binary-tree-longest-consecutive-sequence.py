from typing import List, Optional
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # Find the longest downward path whose child value is exactly parent value + 1.
    # Assumes a nonempty root; O(n) time and O(h) stack space.
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.max_len = 1
        self.dfs(root, 1)
        
        return self.max_len
    
    # curr_len counts the consecutive run ending at this node, not the whole root-to-node path.
    def dfs(self, node, curr_len):

        if node.left is not None:
            # Extend the run only across a +1 edge; otherwise start a new length-one run at that child.
            if node.left.val - node.val == 1:
                self.dfs(node.left, curr_len+1)
            else:
                self.dfs(node.left, 1)
    
        if node.right is not None:
            # Apply the same rule independently to the right branch; paths cannot turn through siblings.
            if node.right.val - node.val == 1:
                self.dfs(node.right, curr_len+1)
            else:
                self.dfs(node.right, 1)

        # Keep a global maximum because the best run may end anywhere, not only at the root or a leaf.
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