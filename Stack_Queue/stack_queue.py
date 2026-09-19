

# Stack
# A stack is LIFO: append and pop at the same end. Python list operations here are amortized O(1).
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.append("Iqbal")
print(stack)

print(stack.pop())

print(stack)

print(stack.pop())

print(stack)

from collections import deque
# Despite the variable name, this first deque example is a stack because it removes with pop().
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.pop())                 
print(queue.pop())                 
print(queue)


# Queue

# A queue is FIFO: append at the right and remove from the left.
# Using list.pop(0) shifts remaining entries, so each dequeue costs O(n).
queue = ["Amar", "Akbar", "Anthony"]
queue.append("Ram")
queue.append("Iqbal")
print(queue)

print(queue.pop(0))

print(queue)

print(queue.pop(0))

print(queue)


from collections import deque
# The final deque example uses append/popleft for FIFO order with O(1) endpoint operations.
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())                 
print(queue.popleft())                 
print(queue)