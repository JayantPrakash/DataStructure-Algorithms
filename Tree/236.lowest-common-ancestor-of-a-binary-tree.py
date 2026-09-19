# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
from typing import Optional

from sqlalchemy import null
from build_tree import build_tree
# Definition for a binary tree node.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Group the state and operations used by the lowest common ancestor of a binary tree implementation.
class Solution:
    # Compute or update the lowest common ancestor result for the supplied input.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  
        self.p_ancs = [] 
        self.q_ancs = []
        self.p = p
        self.q = q 
        self.dfs(root, [])

        self.p_ancs = self.p_ancs[0]
        self.q_ancs = self.q_ancs[0]
        common_ancs = []    
        # Process each value from `range(len(self.p_ancs))`.
        for i in range(len(self.p_ancs)):
            # Process each value from `range(len(self.q_ancs))`.
            for j in range(len(self.q_ancs)):
                # Choose this path when `self.p_ancs[i].val == self.q_ancs[j].val` is true.
                if self.p_ancs[i].val == self.q_ancs[j].val:
                    common_ancs.append(self.p_ancs[i])
        return common_ancs[-1]

    # Traverse the reachable structure using DFS.
    def dfs(self, node, slate):

        slate.append(node)

        # Choose this path when `node.val == self.p.val` is true.
        if node.val == self.p.val:
            self.p_ancs.append(slate[:])

        # Choose this path when `node.val == self.q.val` is true.
        if node.val == self.q.val:
            self.q_ancs.append(slate[:])

        # Choose this path when `node.left is not None` is true.
        if node.left is not None:
            self.dfs(node.left, slate)

        # Choose this path when `node.right is not None` is true.
        if node.right is not None:
            self.dfs(node.right, slate)
        
        slate.pop()


sol = Solution()
list_val = [1,2]
root = build_tree(list_val)
 
print(sol.lowestCommonAncestor(root,TreeNode(1), TreeNode(2)))                  
