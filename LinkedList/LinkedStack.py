# Key idea: Follow pointer updates carefully so links are neither skipped nor lost.
# Group the state and operations used by the LinkedStack implementation.
class LinkedStack:
    # Group the state and operations used by the LinkedStack implementation.
    class _Node:
        # Initialize the state needed by a new instance.
        def __init__(self, element, next):
            self._element = element
            self._next = next

    # Initialize the state needed by a new instance.
    def __init__(self):
        self._head = None
        self._size = 0

    # Compute or update the len result for the supplied input.
    def __len__(self):
        return self._size

    # Compute or update the is empty result for the supplied input.
    def is_empty(self):
        return self._size == 0

    # Compute or update the push result for the supplied input.
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    # Compute or update the pop result for the supplied input.
    def pop(self):
        # Choose this path when `self.is_empty()` is true.
        if self.is_empty():
            return 'Stack is empty'

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    # Compute or update the display result for the supplied input.
    def display(self):
        iter = self._head
        elems = []
        # Keep processing while `iter is not None` remains true.
        while iter is not None:
            elems.append(iter._element)
            iter = iter._next
        return elems

stack = LinkedStack()
stack.push(3)
stack.push(5)
stack.push(8)
stack.pop()
print(stack.display())


