# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Assign positions as if the tree were complete, so gaps between actual nodes count toward width.
    # Only real nodes are enqueued; assumes a nonempty root.
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        # Use one-based positions: a parent's left and right children are 2*id and 2*id+1.
        q.append((root,1))
        max_val = 1    
        while len(q) != 0:
            num_nodes = len(q)
            leftmost, rightmost, first = None, None, None

            for _ in range(num_nodes):
                node, id = q.popleft()

                if node.left is not None:
                    q.append((node.left, 2*id))

                if node.right is not None:
                    q.append((node.right, 2*id+1))

                # The first dequeued position is the leftmost at this depth because children are enqueued left first.
                if first is None:
                    leftmost = id
                    first = id
            
            # The last position consumed in this fixed-size level is its rightmost position.
            rightmost = id        
            # Subtract endpoints and add one to include missing slots between them, not just actual node count.
            local_width = rightmost - leftmost + 1
            if max_val < local_width:
                max_val = local_width    

        # There are O(n) queue visits and O(w) entries; unnormalized positions can grow with tree depth.
        # Python integers avoid overflow, but very deep position values are not constant-size integers.
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
        