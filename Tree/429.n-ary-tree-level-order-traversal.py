from typing import List, Optional
from collections import deque
# Definition for a Node.
# An N-ary node has an ordered list of children; traversal here requires [] for leaves rather than None.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    # BFS batches every depth into one list: O(n) time, O(w) queue space, and O(n) output.
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if root is None:
            return result
        q = deque()
        q.append(root)
        len_q = len(q)

        while len(q) != 0:
            # Capture the current level size before adding any children.
            len_q = len(q)
            temp = []

            for _ in range(len_q):
                node = q.popleft()
                # This stores Node objects, not node.val, despite the List[List[int]] return annotation.
                temp.append(node)

                # Enqueue all children in their supplied order; they form the next level's frontier.
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