# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    
    # Ask whether any complete root-to-leaf path sums to targetSum.
    # O(n) time and O(h) stack space; an empty tree has no qualifying path.
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if root is None:
            return False
        
        self.global_box = False
        self.dfs(root, targetSum)
        return self.global_box
    
    # targetSum is the amount still needed before counting the current node.
    # Each child receives a new numeric remainder, so sibling branches do not need an undo step.
    def dfs(self, node, targetSum):

        # Check equality only at a leaf; matching the target at an internal node is insufficient.
        if node.left is None and node.right is None:
            if targetSum - node.val == 0:
                # Remember a successful path; traversal continues, but later failures cannot reset this flag.
                self.global_box = True

        if node.left is not None:
            # Subtract the current value before descending; negative values are allowed, so do not prune on sign.
            self.dfs(node.left, targetSum - node.val)     

        if node.right is not None:
            self.dfs(node.right, targetSum - node.val)    

    

    