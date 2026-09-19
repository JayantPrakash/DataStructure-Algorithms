from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Inorder traversal of a BST produces values in sorted order; select index k-1.
    # Assumes a nonempty valid BST and 1 <= k <= node count.
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes_val = []
        # This version collects all n values instead of stopping at the kth: O(n) time and O(n) result storage.
        self.dfs(root)
        # Convert the one-based rank to a zero-based list index.
        return self.nodes_val[k-1]

    def dfs(self, node):

        if node.left is not None:
            self.dfs(node.left)
        # The left subtree has already contributed its smaller values; append this node before the larger right subtree.
        self.nodes_val.append(node.val)

        if node.right is not None:
            self.dfs(node.right)

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)     

print(sol.kthSmallest(root,3))                  
                