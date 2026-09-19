# A singly linked node stores a value and the next link; only the head gives access to the chain.
class Node():

    def __init__(self,data):
        self.data = data
        self.next = None

# Prepend in O(1): point the new node to the old head, then return the new head for the caller to retain.
def insert(head,val):
    if head == None:
        head = Node(val)
    else:
        new_node = Node(val)
        new_node.next = head
        head = new_node
    return head

# Following next links visits each node once: O(n) time and O(1) working space.
def print_values(head):
    node = head
    while node is not None:
        print(node.data)
        node = node.next

# Search sequentially because linked lists have no constant-time random access.
# This version assumes head is nonempty.
def search(head, val):
    if head.data == val:
        return True
    else:
        node = head
        while node is not None:
            # This checks object identity, not value equality; equal but distinct objects may fail to match.
            if node.data is val:
                return True
            else:
                node = node.next
    return False

# Delete a one-based position by tracking the target and its predecessor; traversal takes O(n).
def delete(head, position):
    count = 0
    prev = head
    temp = head

    # Removing the first node changes the head itself; the caller must keep the returned reference.
    if position == 1:
        head = head.next
    else:
        for i in range(0,position):
            if i == position - 1 and temp is not None:
                # Bypass the target to preserve the remaining chain without copying any nodes.
                prev.next = temp.next
            else:
                prev = temp
                if prev is None:
                    break
                temp = temp.next
    return head

head = None
head = insert(head,5)
head = insert(head,7)
head = insert(head,9)

print_values(head)

print(search(head,5))
head = (delete(head,3))
print_values(head)