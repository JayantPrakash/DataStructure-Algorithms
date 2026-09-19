
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    # Carry depth downward, counting root as 1; update the global best at leaves.
    # Visiting n nodes takes O(n) time and O(h) call-stack space.
    def dfs(self,node, depth):
        # A leaf has no children; this code expects a list, so children=None is not supported.
        if len(node.children) == 0:
            if self.max_depth < depth:
                self.max_depth = depth
        # Every child is one level deeper; each recursive call receives its own numeric depth.
        for child in node.children:
            self.dfs(child, depth + 1)        

    # Reset the best depth for a new traversal, and handle the empty tree separately.
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.max_depth = 1
        if root is None:
            return 0
        # Starting at one makes a tree with just its root have depth one.
        self.dfs(root,1)
        return self.max_depth
