import heapq

# Creating a list
h = [35, 20, 15, 30, 40]

# Convert the list into a min-heap by default and its inplace
heapq.heapify(h)

print("Heap queue:", h)

# Appending an element
heapq.heappush(h, 5)

# Pop the smallest element from the heap
min = heapq.heappop(h)

print(h)

print("Smallest:", min)
print(h)

# Find the 3 largest elements
maxi = heapq.nlargest(3, h)
print("3 largest elements:", maxi)

# Find the 3 smallest elements
min = heapq.nsmallest(3, h)
print("3 smallest elements:", min)

# Merging Heaps
h2 = [2, 4, 6, 8]

# Merging the lists
h3 = list(heapq.merge(h, h2))
print("Merged heap:", h3)

#priority queue
# list of students
list_stu = [(5,'Rina'),(1,'Anish'),(3,'Moana'),(2,'cathy'),(4,'Lucy')]

# Arrange based on the roll number
heapq.heapify(list_stu)

print("The order of presentation is :")

for i in list_stu:
  print(i[0],':',i[1])

heapq.heappush(list_stu, (7,'Deepak'))
heapq.heappop(list_stu)  

print(list_stu)

# heap sort

def heapsort(h):
    heapq.heapify(h)
    return [heapq.heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))