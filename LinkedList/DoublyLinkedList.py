# Key idea: Follow pointer updates carefully so links are neither skipped nor lost.
# Group the state and operations used by the DoublyLinkedList implementation.
class _DoubleLinekedBase:
    # Group the state and operations used by the DoublyLinkedList implementation.
    class _Node:
        # Initialize the state needed by a new instance.
        def __init__(self, e, prev, next):
            self._element = e
            self._next = next
            self._prev = prev

    # Initialize the state needed by a new instance.
    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)

        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    # Compute or update the len result for the supplied input.
    def __len__(self):
        return self._size

    # Compute or update the is empty result for the supplied input.
    def is_empty(self):
        return self._size == 0

    # Compute or update the insert between result for the supplied input.
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

    # Compute or update the delete node result for the supplied input.
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next

        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        answer = node._element
        node._element = None
        node._prev = None
        node._next = None

        return answer

    # Compute or update the display result for the supplied input.
    def _display(self):
        iter = self._header._next
        elems = []
        # Keep processing while `iter._element != None` remains true.
        while iter._element != None:
            elems.append(iter._element)
            iter = iter._next

        return elems

dll = _DoubleLinekedBase()
#node1 = dll._Node(3,None,None)
dll._insert_between(3, dll._header,dll._trailer)
print(dll._display())
