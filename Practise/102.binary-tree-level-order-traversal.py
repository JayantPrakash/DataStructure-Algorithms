# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Group tree values by depth using BFS: O(n) time, O(w) queue space, and O(n) output.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

      # This practice version returns None for an empty tree, rather than an empty result list.
      if root is None:
          return None

      q = deque()
      q.append(root)
      result = []  
      while(len(q) != 0):
          # Snapshot the number of nodes already queued; children added below belong to the next depth.
          len_q = len(q)
          temp = []  
          for _ in range(len_q):
            node = q.popleft()
            temp.append(node.val)
            # Enqueue children left before right to preserve each level's left-to-right order.
            if node.left is not None:
               q.append(node.left)

            if node.right is not None:
                q.append(node.right)

          # Append after the fixed-size batch, so one inner list represents exactly one level.
          result.append(temp)      
               
      return result

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.levelOrder(root))      