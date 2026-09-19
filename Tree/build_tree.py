# Key idea: Track the current node, the chosen subtree, and the value returned upward.
from collections import deque
from typing import List, Optional


# Group the state and operations used by the build tree implementation.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Compute or update the build tree result for the supplied input.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    # Choose this path when `not values or values[0] is None` is true.
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    parents = deque([root])
    index = 1

    # Keep processing while `parents and index < len(values)` remains true.
    while parents and index < len(values):
        parent = parents.popleft()

        # Choose this path when `values[index] is not None` is true.
        if values[index] is not None:
            parent.left = TreeNode(values[index])
            parents.append(parent.left)
        index += 1

        # Choose this path when `index < len(values) and values[index] is not None` is true.
        if index < len(values) and values[index] is not None:
            parent.right = TreeNode(values[index])
            parents.append(parent.right)
        index += 1

    return root
