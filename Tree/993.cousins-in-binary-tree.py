# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Cousins are at the same depth but have different parents; siblings must be rejected.
    # BFS checks both properties in O(n) time and O(w) space; assumes a nonempty root and unique values.
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:  
        q = deque()
        q.append(root)
        while len(q) != 0:
            len_q = len(q)
            # Reset both parent records each level so discoveries at different depths cannot be combined.
            parent_x = None
            parent_y = None

            for _ in range(len_q):
                node = q.popleft()

                if node.left is not None:
                    q.append(node.left)
                    # Record the parent while examining its children; all children in this batch share the next depth.
                    if node.left.val == x:
                        parent_x = node
                    if node.left.val == y:
                        parent_y = node   
            
                if node.right is not None:
                    q.append(node.right)
                    if node.right.val == x:
                        parent_x = node
                    if node.right.val == y:
                        parent_y = node   
            
            # Both targets were found among this level's children, and their parent identities differ.
            if (parent_x is not None) and (parent_y is not None) and parent_x != parent_y:
                return True
        
        # The root has no parent and cannot be a cousin; unmatched depths or equal parents never satisfy the test.
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