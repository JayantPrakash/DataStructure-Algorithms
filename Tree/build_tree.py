from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Interpret values as compact level-order data, using None for a missing child.
# Only real nodes enter the parent queue; missing nodes do not consume their own child slots.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    # The queue contains real nodes still waiting for left/right children from the input stream.
    parents = deque([root])
    index = 1

    while parents and index < len(values):
        parent = parents.popleft()

        # The next entry is this parent's left slot; advance the index even when the slot is absent.
        if values[index] is not None:
            parent.left = TreeNode(values[index])
            parents.append(parent.left)
        index += 1

        # The following entry is its right slot, if supplied; queue each real child for later expansion.
        if index < len(values) and values[index] is not None:
            parent.right = TreeNode(values[index])
            parents.append(parent.right)
        index += 1

    # Construction is O(m) in consumed input entries, with O(w) parent queue space plus allocated nodes.
    return root
