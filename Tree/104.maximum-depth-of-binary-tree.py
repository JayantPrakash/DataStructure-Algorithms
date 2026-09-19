# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Maximum depth is the number of nonempty levels; this implementation counts them with BFS.
    # O(n) time and O(w) queue space; an empty tree has depth zero.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        level = 0
        q = deque()
        q.append(root)
        len_q = len(q)

        while len(q) != 0:
            len_q = len(q)
            # Increment once per level, not per node: all nodes in this batch share the same depth.
            level += 1
            # Only consume nodes present when the batch began; enqueued children belong to the next depth.
            for _ in range(len_q):
                node = q.popleft()

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
        
        # When the queue empties, the number of completed batches is the deepest root-to-leaf node count.
        return level       

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.maxDepth(root))                            

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""