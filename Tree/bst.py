# Key idea: Track the current node, the chosen subtree, and the value returned upward.
# Group the state and operations used by the bst implementation.
class BST:
    # Initialize the state needed by a new instance.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Compute or update the insert result for the supplied input.
    def insert(self, value):
        currentNode = self
        # Keep processing while `True` remains true.
        while True:
            # Choose this path when `currentNode.value > value` is true.
            if currentNode.value > value:
                previous = currentNode
                currentNode = currentNode.left

                # Choose this path when `currentNode is None` is true.
                if currentNode is None:
                    previous.left = BST(value)
                    break
            else:
                previous = currentNode
                currentNode = currentNode.right
                # Choose this path when `currentNode is None` is true.
                if currentNode is None:
                    previous.right = BST(value)
                    break

    # Compute or update the contains result for the supplied input.
    def contains(self, value):
        # Choose this path when `self.value == value` is true.
        if self.value == value:
            return True

        # Choose this path when `self.value > value` is true.
        if self.value > value:
            # Choose this path when `self.left is None` is true.
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            # Choose this path when `self.right is None` is true.
            if self.right is None:
                return False
            else:
                return self.right.contains(value)




    # Compute or update the inorder recursive result for the supplied input.
    def inorder_recursive(self, temp):
        # Choose this path when `temp is None` is true.
        if temp is None:
            return

        self.inorder_recursive(temp.left)
        print(temp.value, end = " ")
        self.inorder_recursive(temp.right)


#r = BST(3)
#r.insert(5)
#r.insert(2)
#r.inorder_recursive(r)

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

root.insert(12)
print('contains::',root.contains(55))
print(root.right.left.left.value == 12)
root.inorder_recursive(root)