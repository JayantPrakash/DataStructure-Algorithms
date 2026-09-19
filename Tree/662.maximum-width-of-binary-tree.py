# Key idea: Track the current node, the chosen subtree, and the value returned upward.
# Definition for a binary tree node.
from typing import Optional
from collections import deque

# Group the state and operations used by the maximum width of binary tree implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the maximum width of binary tree implementation.
class Solution:
    # Compute or update the width of binary tree result for the supplied input.
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root,1))
        max_val = 1    
        # Keep processing while `len(q) != 0` remains true.
        while len(q) != 0:
            num_nodes = len(q)
            leftmost, rightmost, first = None, None, None

            # Process each value from `range(num_nodes)`.
            for _ in range(num_nodes):
                node, id = q.popleft()

                # Choose this path when `node.left is not None` is true.
                if node.left is not None:
                    q.append((node.left, 2*id))

                # Choose this path when `node.right is not None` is true.
                if node.right is not None:
                    q.append((node.right, 2*id+1))

                # Choose this path when `first is None` is true.
                if first is None:
                    leftmost = id
                    first = id
            
            rightmost = id        
            local_width = rightmost - leftmost + 1
            # Choose this path when `max_val < local_width` is true.
            if max_val < local_width:
                max_val = local_width    

        return max_val


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.widthOfBinaryTree(root))                            

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    

Note: here every node in queue will be stored as tuple(node and id associated with that node)
keep three pointers, leftmost,right most and first
leftmost_id = first id in that level, if first is none, assign it to left
rightmost_id = last id in that level
at every node, id of left node will be 2* parent id of that node
id of right node will be 2* parent id of that node + 1
local_width = rightmost-leftmost + 1
"""
        