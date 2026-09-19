# Key idea: Follow pointer updates carefully so links are neither skipped nor lost.
# a linked list node
class Node:
    # Initialize the state needed by a new instance.
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# function to traverse and print the singly linked list
def traverseList(head):
    # Keep processing while `head is not None` remains true.
    while head is not None:
        print(head.data, end=" ")
        head = head.next

# Run this example only when the file is executed directly.
if __name__ == "__main__":

    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    traverseList(head)