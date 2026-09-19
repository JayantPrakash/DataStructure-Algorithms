# Key idea: Track the current node, the chosen subtree, and the value returned upward.
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

# Group the state and operations used by the average of levels in binary tree implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the average of levels in binary tree implementation.
class Solution:
    # Compute or update the average of levels result for the supplied input.
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        q = deque()
        q.append(root)
        len_q = len(q)

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

            temp = sum(temp)/len_q
            result.append(temp)
        return result       

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.averageOfLevels(root))                            

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""