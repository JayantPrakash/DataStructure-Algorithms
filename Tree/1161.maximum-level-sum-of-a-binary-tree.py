# Key idea: Track the current node, the chosen subtree, and the value returned upward.
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque
from math import inf
# Group the state and operations used by the maximum level sum of a binary tree implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the maximum level sum of a binary tree implementation.
class Solution:
    # Compute or update the max level sum result for the supplied input.
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        small_level = 1
        curr_level = 1
        max_sum = -inf
        
        q = deque()
        q.append(root)

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

            temp_sum = sum(temp)
            # Choose this path when `temp_sum > max_sum` is true.
            if temp_sum > max_sum:
                small_level = curr_level
                max_sum = temp_sum
            curr_level += 1

        return small_level                       
                
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.maxLevelSum(root))                  
                
"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
                     
Note:

Don't assume max_sum to be 0, assume it to be -inf as all values can be negative in tree

"""   