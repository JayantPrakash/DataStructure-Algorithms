# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Use ordinary BFS, then reverse alternate output rows to create zigzag order.
    # All node visits and reversals total O(n) time; the queue uses O(w) space.
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return result

        q = deque()
        q.append(root)
        reverse = False
        while len(q) != 0:
            # Snapshot this level before enqueueing children from it.
            len_q = len(q)

            temp = []

            for _ in range(len_q):
                node = q.popleft()
                temp.append(node.val)

                # Always discover left before right; the direction change belongs to output formatting only.
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            # Leave the root row forward, then alternate forward/reversed rows.
            if not reverse:
                reverse = True
            else:    
                # Reverse the completed level's values without rearranging the queue or tree.
                temp.reverse()
                reverse = False    
            
            result.append(temp)            
        return result
    
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.zigzagLevelOrder(root))                  
                
"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""            
        

