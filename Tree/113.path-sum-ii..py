# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
# Definition for a binary tree node.
class TreeNode(object):
     # Initialize the state needed by a new instance.
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Group the state and operations used by the path sum ii implementation.
class Solution(object):
    
    # Compute or update the has path sum result for the supplied input.
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        # Choose this path when `root is None` is true.
        if root is None:
            return []
        
        self.global_box = []
        self.dfs(root, targetSum, [])
        return self.global_box
    
    # Traverse the reachable structure using DFS.
    def dfs(self, node, targetSum, slate):
        slate.append(node.val)
        # Choose this path when `node.left is None and node.right is None` is true.
        if node.left is None and node.right is None:
            # Choose this path when `targetSum - node.val == 0` is true.
            if targetSum - node.val == 0:
                self.global_box.append(slate[:])

        # Choose this path when `node.left is not None` is true.
        if node.left is not None:
            self.dfs(node.left, targetSum - node.val, slate)     

        # Choose this path when `node.right is not None` is true.
        if node.right is not None:
            self.dfs(node.right, targetSum - node.val, slate)    

        slate.pop()

    