# a linked list node
# Each node owns a value and one link; None marks the end rather than an allocated sentinel.
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# function to traverse and print the singly linked list
# Follow links until the end: O(n) time and O(1) extra space for an acyclic list.
def traverseList(head):
    while head is not None:
        print(head.data, end=" ")
        # Advance the local cursor; the caller's head reference and node links are not changed.
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