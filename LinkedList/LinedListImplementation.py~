class Node():

    def __init__(self,data):
        self.data = data
        self.next = None

def insert(head,val):
    if head == None:
        head = Node(val)
    else:
        new_node = Node(val)
        new_node.next = head
        head = new_node
    return head

def print_values(head):
    node = head
    while node is not None:
        print(node.data)
        node = node.next

def search(head, val):
    if head.data == val:
        return True
    else:
        node = head
        while node is not None:
            if node.data is val:
                return True
            else:
                node = node.next
    return False

def delete(head, position):
    count = 0
    prev = head
    temp = head

    if position == 1:
        head = head.next
    else:
        for i in range(0,position):
            if i == position - 1 and temp is not None:
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