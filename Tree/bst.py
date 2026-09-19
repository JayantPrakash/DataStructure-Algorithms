class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if currentNode.value > value:
                previous = currentNode
                currentNode = currentNode.left

                if currentNode is None:
                    previous.left = BST(value)
                    break
            else:
                previous = currentNode
                currentNode = currentNode.right
                if currentNode is None:
                    previous.right = BST(value)
                    break

    def contains(self, value):
        if self.value == value:
            return True

        if self.value > value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)




    def inorder_recursive(self, temp):
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