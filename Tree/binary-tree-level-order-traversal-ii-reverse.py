# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Collect BFS levels, reverse each row, then reverse the row order.
    # This produces bottom-to-top, right-to-left output, unlike standard bottom-up level order.
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        q = deque()
        q.append(root)

        while len(q) != 0:
            # Freeze this level's node count so children are processed in the next batch.
            len_q = len(q)
            temp = []

            for _ in range(len_q):
                node = q.popleft()
                temp.append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            # Reverse horizontal order within the just-completed level.
            temp.reverse()
            result.append(temp)

        # Reverse vertical order across levels; O(n) total time and O(n) output, plus O(w) queue space.
        result.reverse()

        return result

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.levelOrderBottom(root))                  
                
"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""        