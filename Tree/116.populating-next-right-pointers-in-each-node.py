# Key idea: Track the current node, the chosen subtree, and the value returned upward.
from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    # Initialize the state needed by a new instance.
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Group the state and operations used by the populating next right pointers in each node implementation.
class Solution:
    # Compute or update the connect result for the supplied input.
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Choose this path when `root is None` is true.
        if root is None:
            return []
        
        q = deque()
        q.append(root)

        # Keep processing while `len(q) != 0` remains true.
        while len(q) != 0:
            num_nodes = len(q)

            # Process each value from `range(len(q))`.
            for i in range(len(q)):
                node = q.popleft()

                # Choose this path when `node.left is not None` is true.
                if node.left is not None:
                    q.append(node.left)
                # Choose this path when `node.right is not None` is true.
                if node.right is not None:    
                    q.append(node.right)

                #first node of level, only capture prev
                if i == 0:
                    prev_node = node
                # non first level of each node, connect prev next to the current node
                else:
                    prev_node.next = node
                    prev_node = node

            # make next of last node of level to None 
            prev_node = None
        return root

sol = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)     

print(sol.connect(root))                            

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
Note: if it is the first node in the level, just capture prev node only,
otherwsise make the prevnode next to the current node and prev node to the current node
At the end of level, make prev node next equivalent to None
        if i == 0:
            prev_node = node
        else:
            prev_node.next = node
            prev_node = node

prev_node = None
"""        