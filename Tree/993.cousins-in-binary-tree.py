# Key idea: Track the current node, the chosen subtree, and the value returned upward.
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

# Group the state and operations used by the cousins in binary tree implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the cousins in binary tree implementation.
class Solution:
    # Compute or update the is cousins result for the supplied input.
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:  
        q = deque()
        q.append(root)
        # Keep processing while `len(q) != 0` remains true.
        while len(q) != 0:
            len_q = len(q)
            parent_x = None
            parent_y = None

            # Process each value from `range(len_q)`.
            for _ in range(len_q):
                node = q.popleft()

                # Choose this path when `node.left is not None` is true.
                if node.left is not None:
                    q.append(node.left)
                    # Choose this path when `node.left.val == x` is true.
                    if node.left.val == x:
                        parent_x = node
                    # Choose this path when `node.left.val == y` is true.
                    if node.left.val == y:
                        parent_y = node   
            
                # Choose this path when `node.right is not None` is true.
                if node.right is not None:
                    q.append(node.right)
                    # Choose this path when `node.right.val == x` is true.
                    if node.right.val == x:
                        parent_x = node
                    # Choose this path when `node.right.val == y` is true.
                    if node.right.val == y:
                        parent_y = node   
            
            # Choose this path when `parent_x is not None and parent_y is not None and (parent_x != parent_y)` is true.
            if (parent_x is not None) and (parent_y is not None) and parent_x != parent_y:
                return True
        
        return False                       
                
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.isCousins(root, 4, 1))                  
                
"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    

Note:

initialize parent_x and parent_y at every level, so no need to track level
"""                        