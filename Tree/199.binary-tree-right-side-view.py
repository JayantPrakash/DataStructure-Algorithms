# Key idea: Trace the queue one breadth-first level at a time.
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

# Group the state and operations used by the binary tree right side view implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the binary tree right side view implementation.
class Solution:
    # Compute or update the right side view result for the supplied input.
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # Choose this path when `root is None` is true.
        if root is None:
            return result
        
        q = deque()
        q.append(root)

        # Keep processing while `len(q) != 0` remains true.
        while len(q) != 0:
            len_q = len(q)

            temp = []

            # Process each value from `range(len_q)`.
            for _ in range(len_q):
                node = q.popleft()
                temp.append(node.val)

                # Choose this path when `node.left is not None` is true.
                if node.left is not None:
                    q.append(node.left)

                # Choose this path when `node.right is not None` is true.
                if node.right is not None:
                    q.append(node.right)

            result.append(temp[-1])
        return result                       
                
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.rightSideView(root))                  
                
"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""                        