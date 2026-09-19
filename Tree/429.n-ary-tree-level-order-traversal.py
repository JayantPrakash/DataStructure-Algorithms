# Key idea: Trace the queue one breadth-first level at a time.
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque
# Definition for a Node.
class Node:
    # Initialize the state needed by a new instance.
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

# Group the state and operations used by the n ary tree level order traversal implementation.
class Solution:
    # Compute or update the level order result for the supplied input.
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        # Choose this path when `root is None` is true.
        if root is None:
            return result
        q = deque()
        q.append(root)
        len_q = len(q)

        # Keep processing while `len(q) != 0` remains true.
        while len(q) != 0:
            len_q = len(q)
            temp = []

            # Process each value from `range(len_q)`.
            for _ in range(len_q):
                node = q.popleft
                temp.append(node)

                # Process each value from `node.children`.
                for child in node.children:
                    q.append(child)

            result.append(temp)
        return result            
    

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""