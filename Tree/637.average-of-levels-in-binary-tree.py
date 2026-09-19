# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Process one BFS level at a time, then divide its value sum by its node count.
    # Assumes a nonempty root; O(n) time and O(w) temporary space.
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        q = deque()
        q.append(root)
        len_q = len(q)

        # The queue begins each batch with exactly one depth's nodes.
        while len(q) != 0:
            len_q = len(q)
            temp = []

            # Use the original batch size so children discovered now belong to the next average.
            for _ in range(len_q):
                node = q.popleft()
                temp.append(node.val)


                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            # Divide by this level's count, not the changing queue length, which now includes children.
            temp = sum(temp)/len_q
            result.append(temp)
        return result       

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.averageOfLevels(root))                            

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""