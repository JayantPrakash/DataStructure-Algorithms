# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # BFS visits shallower depths first, so the first leaf encountered gives the minimum depth.
    # Worst-case O(n) time and O(w) queue space; the root is depth 1.
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        level = 0
        q = deque()
        q.append(root)
        len_q = len(q)

        while len(q) != 0:
            len_q = len(q)
            # Every node in the frozen queue batch belongs to this same depth.
            level += 1
            for _ in range(len_q):
                node = q.popleft()

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
            
                # A leaf has no children at all; one missing child must not terminate a root-to-leaf path.
                if node.left is None and node.right is None:
                    # Return immediately for the first leaf; all undiscovered leaves are at least this deep.
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