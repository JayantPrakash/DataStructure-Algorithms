# Definition for a binary tree node.
from typing import List, Optional
from collections import deque     

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    # Find one maximum for each BFS level; O(n) time and O(w) queue space.
    def largestValues(self, root: TreeNode | None) -> list[int]:
        result = []
        if root is None: return []
        q = deque()
        q.append(root)
        len_q = len(q)

        while len(q) != 0:
            len_q = len(q)
            # Reset below every possible value at each level so negative-only rows work correctly.
            largest = float("-inf")
            # Process exactly the nodes already in this level; newly enqueued children wait for the next row.
            for _ in range(len_q):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
                # Maintain the maximum over just the current batch.
                largest = max(largest, node.val)    
            # Append after the entire row is consumed so there is exactly one answer per depth.
            result.append(largest)
        return result       