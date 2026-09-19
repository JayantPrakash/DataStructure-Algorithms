# Header and trailer sentinels remove special cases at the ends: real nodes always have two neighbors.
class _DoubleLinekedBase:
    class _Node:
        def __init__(self, e, prev, next):
            self._element = e
            self._next = next
            self._prev = prev

    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)

        # An empty list links the sentinels directly; neither sentinel represents user data.
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # Insert between adjacent nodes in O(1): connect the new node in both directions and repair both neighbors.
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

    # Delete a real, linked node in O(1); sentinel nodes must never be passed here.
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next

        # Bypass the removed node in both directions so forward and backward traversal remain consistent.
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        answer = node._element
        # Clear the removed node's references after saving its value; it is no longer part of the list.
        node._element = None
        node._prev = None
        node._next = None

        return answer

    # Walk from the first real node to the trailer in O(n).
    # This implementation uses element == None as the stopping marker, so a real None value stops display early.
    def _display(self):
        iter = self._header._next
        elems = []
        while iter._element != None:
            elems.append(iter._element)
            iter = iter._next

        return elems

dll = _DoubleLinekedBase()
#node1 = dll._Node(3,None,None)
dll._insert_between(3, dll._header,dll._trailer)
print(dll._display())
