# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    
    # Collect all qualifying root-to-leaf paths, despite the boolean-like method name/type notes.
    # O(n + P) time for traversal plus P copied output values; O(h) working path/stack space.
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if root is None:
            return []
        
        self.global_box = []
        self.dfs(root, targetSum, [])
        return self.global_box
    
    # targetSum is the remaining sum before this node; slate tracks its ancestor path.
    def dfs(self, node, targetSum, slate):
        # Choose this node before exploring either child so both branches inherit the root-to-current path.
        slate.append(node.val)
        if node.left is None and node.right is None:
            if targetSum - node.val == 0:
                # At a leaf with zero remainder, save a copy; later backtracking must not alter this answer.
                self.global_box.append(slate[:])

        if node.left is not None:
            self.dfs(node.left, targetSum - node.val, slate)     

        if node.right is not None:
            self.dfs(node.right, targetSum - node.val, slate)    

        # Undo the current node after both children, restoring the exact ancestor path for the caller.
        slate.pop()

    