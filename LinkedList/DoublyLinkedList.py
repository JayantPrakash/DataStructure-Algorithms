class _DoubleLinekedBase:
    class _Node:
        def __init__(self, e, prev, next):
            self._element = e
            self._next = next
            self._prev = prev

    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)

        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

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
