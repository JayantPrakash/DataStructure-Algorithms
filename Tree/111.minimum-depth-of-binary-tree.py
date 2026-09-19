# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

# Group the state and operations used by the minimum depth of binary tree implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the minimum depth of binary tree implementation.
class Solution:
    # Compute or update the min depth result for the supplied input.
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Choose this path when `root is None` is true.
        if root is None:
            return 0
        level = 0
        q = deque()
        q.append(root)
        len_q = len(q)

        # Keep processing while `len(q) != 0` remains true.
        while len(q) != 0:
            len_q = len(q)
            level += 1
            # Process each value from `range(len_q)`.
            for _ in range(len_q):
                node = q.popleft()

                # Choose this path when `node.left is not None` is true.
                if node.left is not None:
                    q.append(node.left)

                # Choose this path when `node.right is not None` is true.
                if node.right is not None:
                    q.append(node.right)
            
                # This is the leaf condition
                if node.left is None and node.right is None:
                    return level
        
        return level       

sol = Solution()
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.minDepth(root))                            

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""