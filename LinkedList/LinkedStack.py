# Use the head as the stack top: the most recently pushed element is removed first (LIFO).
# Push and pop take O(1); the linked nodes use O(n) total space.
class LinkedStack:
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        # Link the new node to the old head before replacing the head reference, preserving the chain.
        self._head = self._Node(e, self._head)
        self._size += 1

    # Guard the empty case before reading the top; this version returns a message string when empty.
    def pop(self):
        if self.is_empty():
            return 'Stack is empty'

        answer = self._head._element
        # Unlink the old top by moving head to its successor; no traversal is needed.
        self._head = self._head._next
        self._size -= 1
        return answer

    # Walk from top toward bottom without changing stack state; building the result takes O(n) space.
    def display(self):
        iter = self._head
        elems = []
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


