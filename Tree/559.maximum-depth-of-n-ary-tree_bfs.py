from typing import List, Optional
from collections import deque
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    # Count BFS batches to obtain the maximum number of nodes on a root-to-leaf path.
    # O(n) time and O(w) frontier space; an empty tree has depth zero.
    def maxDepth(self, root: Optional[Node]) -> int:
        if root is None:
            return 0
        level = 0
        q = deque()
        q.append(root)
        len_q = len(q)

        while len(q) != 0:
            len_q = len(q)
            # All nodes already queued belong to one depth, so increment once before consuming that batch.
            level += 1
            for _ in range(len_q):
                node = q.popleft()

                # Enqueue all children for the next depth; leaf children must be an empty iterable, not None.
                for child in node.children:
                    q.append(child)
        
        # After the last frontier is consumed, the batch count is the deepest level.
        return level    