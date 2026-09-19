# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # A node is good when no ancestor on its own root-to-node path has a larger value.
    # This version assumes a nonempty root and explicitly stores that path.
    def goodNodes(self, root: TreeNode) -> int:

        self.count_good_nodes = 0

        self.dfs(root, slate = [])

        return self.count_good_nodes
    
    def dfs(self, node, slate):
        # Extend the path for this node; child calls must remove their own additions before returning.
        slate.append(node.val)

        if node.left is not None:
            self.dfs(node.left, slate)

        if node.right is not None:
            self.dfs(node.right, slate)

        # After children backtrack, slate again contains only this node and its ancestors.
        # Scanning max(slate) at every node costs O(nh), up to O(n^2); a carried path maximum would avoid rescanning.
        if node.val >= max(slate):
            self.count_good_nodes += 1

        # Restore the parent's path so sibling branches do not see each other's values.
        slate.pop()            

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.goodNodes(root))           