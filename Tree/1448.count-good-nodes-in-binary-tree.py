# Key idea: Track the current node, the chosen subtree, and the value returned upward.
# Definition for a binary tree node.
class TreeNode:
    # Initialize the state needed by a new instance.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the count good nodes in binary tree implementation.
class Solution:
    # Compute or update the good nodes result for the supplied input.
    def goodNodes(self, root: TreeNode) -> int:

        self.count_good_nodes = 0

        self.dfs(root, slate = [])

        return self.count_good_nodes
    
    # Traverse the reachable structure using DFS.
    def dfs(self, node, slate):
        slate.append(node.val)

        # Choose this path when `node.left is not None` is true.
        if node.left is not None:
            self.dfs(node.left, slate)

        # Choose this path when `node.right is not None` is true.
        if node.right is not None:
            self.dfs(node.right, slate)

        # Choose this path when `node.val >= max(slate)` is true.
        if node.val >= max(slate):
            self.count_good_nodes += 1

        slate.pop()            

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.goodNodes(root))           