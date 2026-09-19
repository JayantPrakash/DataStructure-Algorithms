# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
"""
Question:
Given the roots of two binary trees p and q, write a function to 
check if they are the same or not.
Two binary trees are considered the same if they 
are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
from collections import deque

from build_tree import build_tree
# Group the state and operations used by the same tree dfs implementation.
class TreeNode(object):
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the same tree dfs implementation.
class Solution(object):
    # Compute or update the is same tree result for the supplied input.
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        self.is_same = True

        # Choose this path when `p is None and q is None` is true.
        if p is None and q is None:
            return True
        
        # Choose this path when `p is not None and q is None or (p is None and q is not None)` is true.
        if p is not None and q is None or p is None and q is not None :  
            return False   
        
        self.dfs(p,q)

        return self.is_same
    
    # Traverse the reachable structure using DFS.
    def dfs(self, p,q):

        # Choose this path when `p.val != q.val` is true.
        if p.val != q.val:
            self.is_same = False
            return False
        
        # Choose this path when `p.left is None and q.left is None and (p.right is None) and (q.right is ...` is true.
        if p.left is None and q.left is None and p.right is None and q.right is None:
            return True
    
        # Choose this path when `p.left is not None and q.left is None or (p.left is None and q.left is n...` is true.
        if p.left is not None and q.left is None or p.left is None and q.left is not None :  
            self.is_same = False
            return False   
            
        # Choose this path when `p.right is not None and q.right is None or (p.right is None and q.right ...` is true.
        if p.right is not None and q.right is None or  p.right is None and q.right is not None :  
            self.is_same = False
            return False
        
        
        
        is_left_tree_same = True
        is_right_tree_same = True
        # Choose this path when `p.left and q.left` is true.
        if p.left and q.left:
            is_left_tree_same = self.dfs(p.left, q.left)

        # Choose this path when `p.right and q.right` is true.
        if p.right and q.right:
            is_right_tree_same = self.dfs(p.right, q.right)

        # Choose this path when `is_left_tree_same and is_right_tree_same` is true.
        if is_left_tree_same and is_right_tree_same:
            return True
        else:
            self.is_same = False
            return False


sol = Solution()
p = [1,2,3]
p = [1,2]
q = [1,None,2]
rootp = build_tree(p)
#q = [1,2,3]
rootq = build_tree(q) 

print(sol.isSameTree(rootp, rootq))                  

"""
Logic:
Time and space complexity
T(n) = O(n)
S(n) = O(n)
"""