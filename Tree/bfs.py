# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

# Represents one node in a binary tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Use a FIFO queue to visit parents before descendants, producing one flat BFS sequence.
    # O(n) time and O(w) queue space, plus O(n) output; the annotation suggests nested lists but the result is flat.
    def bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        # An empty input returns immediately; the while behaves as a one-time guard because its body returns.
        while root is None:
            return []

        q = deque()
        q.append(root)

        while len(q) != 0:
            # Process the oldest discovered node first; children are scheduled after all earlier frontier nodes.
            node = q.popleft()
            result.append(node.val)

            # Enqueue left before right so values within each depth appear left-to-right.
            if node.left is not None:
                q.append(node.left)

            # The right child follows its left sibling; no visited set is needed for an acyclic tree.
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
