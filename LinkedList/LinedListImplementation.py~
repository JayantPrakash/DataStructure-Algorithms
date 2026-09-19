# Key idea: Follow pointer updates carefully so links are neither skipped nor lost.
# Group the state and operations used by the LinedListImplementation implementation.
class Node():

    # Initialize the state needed by a new instance.
    def __init__(self,data):
        self.data = data
        self.next = None

# Compute or update the insert result for the supplied input.
def insert(head,val):
    # Choose this path when `head == None` is true.
    if head == None:
        head = Node(val)
    else:
        new_node = Node(val)
        new_node.next = head
        head = new_node
    return head

# Compute or update the print values result for the supplied input.
def print_values(head):
    node = head
    # Keep processing while `node is not None` remains true.
    while node is not None:
        print(node.data)
        node = node.next

# Compute or update the search result for the supplied input.
def search(head, val):
    # Choose this path when `head.data == val` is true.
    if head.data == val:
        return True
    else:
        node = head
        # Keep processing while `node is not None` remains true.
        while node is not None:
            # Choose this path when `node.data is val` is true.
            if node.data is val:
                return True
            else:
                node = node.next
    return False

# Compute or update the delete result for the supplied input.
def delete(head, position):
    count = 0
    prev = head
    temp = head

    # Choose this path when `position == 1` is true.
    if position == 1:
        head = head.next
    else:
        # Process each value from `range(0, position)`.
        for i in range(0,position):
            # Choose this path when `i == position - 1 and temp is not None` is true.
            if i == position - 1 and temp is not None:
                prev.next = temp.next
            else:
                prev = temp
                # Choose this path when `prev is None` is true.
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