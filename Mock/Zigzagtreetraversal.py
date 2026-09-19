# Key idea: Trace the queue one breadth-first level at a time.
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

# Group the state and operations used by the Zigzagtreetraversal implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the Zigzagtreetraversal implementation.
class Solution:
    # Compute or update the zigzag level order result for the supplied input.
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Choose this path when `root is None` is true.
        if root is None:
            return []

        q = deque()
        q.append(root)
        result = []
        flag = True
        # Keep processing while `len(q) != 0` remains true.
        while(len(q) != 0):
            num_nodes = len(q)
            temp = []
            # Process each value from `range(num_nodes)`.
            for _ in range(num_nodes):
                node = q.popleft()
                temp.append(node.val)
                # Choose this path when `node.left is not None` is true.
                if node.left is not None:
                    q.append(node.left)

                # Choose this path when `node.right is not None` is true.
                if node.right is not None:
                    q.append(node.right)

            # Choose this path when `flag` is true.
            if flag:
                flag = False
            else:    
                temp.reverse()
                flag = True   

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

                
#T(n) = O(n)
#S(n) = O(n)                