# Key idea: Trace the queue one breadth-first level at a time.
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

# Represents one node in a binary tree.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Group the state and operations used by the bfs implementation.
class Solution:
    # Traverse the tree level by level using breadth-first search (BFS).
    def bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        # An empty tree has no values to return.
        while root is None:
            return []

        # The queue stores nodes that still need to be visited.
        q = deque()
        q.append(root)

        # Continue until every reachable node has been processed.
        while len(q) != 0:
            # Remove the oldest node so nodes are processed from left to right.
            node = q.popleft()
            result.append(node.val)

            # Add the left child to the queue if it exists.
            if node.left is not None:
                q.append(node.left)

            # Add the right child to the queue if it exists.
            if node.right is not None:
                q.append(node.right)

        return result

# Build an example binary tree:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

# Print the values in BFS order: [1, 2, 3, 4, 5, 6].
print(sol.bfs(root))

# Time and space complexity:
# Time: O(n), because each node is visited once.
# Space: O(n), for the queue and the result list in the worst case.
