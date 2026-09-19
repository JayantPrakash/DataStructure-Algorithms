from typing import Optional

from sqlalchemy import null
from build_tree import build_tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Record root-to-target paths, then return the deepest shared ancestor.
    # This version matches nodes by value, so it assumes unique values, both targets present, and a nonempty root.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  
        self.p_ancs = [] 
        self.q_ancs = []
        self.p = p
        self.q = q 
        self.dfs(root, [])

        self.p_ancs = self.p_ancs[0]
        self.q_ancs = self.q_ancs[0]
        common_ancs = []    
        # Compare both saved paths; this nested comparison costs O(h^2) in addition to O(n) traversal.
        for i in range(len(self.p_ancs)):
            for j in range(len(self.q_ancs)):
                if self.p_ancs[i].val == self.q_ancs[j].val:
                    common_ancs.append(self.p_ancs[i])
        # Ancestors were visited root-first, so the last common entry is deepest; a target may be its own ancestor.
        return common_ancs[-1]

    def dfs(self, node, slate):

        # Track node objects, not just values, so the result can return an ancestor node.
        slate.append(node)

        if node.val == self.p.val:
            # Copy the current path when p is found; q uses the same snapshot rule.
            self.p_ancs.append(slate[:])

        if node.val == self.q.val:
            self.q_ancs.append(slate[:])

        if node.left is not None:
            self.dfs(node.left, slate)

        if node.right is not None:
            self.dfs(node.right, slate)
        
        # Backtrack after both children so sibling paths contain only their own ancestors.
        slate.pop()


sol = Solution()
list_val = [1,2]
root = build_tree(list_val)
 
print(sol.lowestCommonAncestor(root,TreeNode(1), TreeNode(2)))                  
