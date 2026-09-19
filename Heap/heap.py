# Key idea: Track heap ordering and which element is kept at the root.
# Group the state and operations used by the heap implementation.
class MaxHeap:
    arr = []
    maxSize = 0
    heapSize = 0

    # Initialize the state needed by a new instance.
    def __init__(self, maxsize):
        self.maxSize = maxsize
        self.heapSize = 0
        self.arr = [None] * maxsize

    # Compute or update the left result for the supplied input.
    def left(self, i):
        return 2 * i + 1

    # Compute or update the right result for the supplied input.
    def right(self, i):
        return 2 * i + 2

    # Compute or update the parent result for the supplied input.
    def parent(self, i):
        return int((i - 1) / 2)

    # Compute or update the max heapify result for the supplied input.
    def MaxHeapify(self, i):
        l = self.left(i)
        r = self.right(i)

        largest = i

        # Choose this path when `self.heapSize == 0 or self.heapSize == 1` is true.
        if self.heapSize == 0 or self.heapSize == 1:
            return

        # Choose this path when `l < self.heapSize and self.arr[l] > self.arr[largest]` is true.
        if l < self.heapSize and self.arr[l] > self.arr[largest]:
            largest = l

        # Choose this path when `r < self.heapSize and self.arr[r] > self.arr[largest]` is true.
        if r < self.heapSize and self.arr[r] > self.arr[largest]:
            largest = r

        # Choose this path when `largest != i` is true.
        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.MaxHeapify(largest)

    # Compute or update the remove max result for the supplied input.
    def removeMax(self):
        # Choose this path when `self.heapSize == 0` is true.
        if self.heapSize == 0:
            return None
        root = self.arr[0]
        # Choose this path when `self.heapSize == 1` is true.
        if self.heapSize == 1:
            self.arr[0] = None
            self.heapSize -= 1
            return root

        self.arr[0] = self.arr[self.heapSize - 1]
        self.heapSize -= 1
        self.MaxHeapify(0)

    # Compute or update the insert key result for the supplied input.
    def insertKey(self, x):
        # Choose this path when `self.heapSize == self.maxSize` is true.
        if self.heapSize == self.maxSize:
            return 'Max elem reached'

        self.heapSize += 1
        i = self.heapSize - 1
        self.arr[i] = x

        # Keep processing while `i != 0 and self.arr[self.parent(i)] < self.arr[i]` remains true.
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = self.arr[i]
            self.arr[i] = temp
            i = self.parent(i)

    # Compute or update the cur size result for the supplied input.
    def curSize(self):
        return self.heapSize

    # Compute or update the get max result for the supplied input.
    def getMax(self):
        return self.arr[0]

    # Compute or update the heap sort result for the supplied input.
    def heapSort(self,arr):
        N = self.heapSize

        # Build a maxheap.
        for i in range(N // 2 - 1, -1, -1):
            self.MaxHeapify(i)

        # One by one extract elements
        for i in range(N - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]  # swap
            self.MaxHeapify(i)
# Driver program to test above functions.
if __name__ == '__main__':
    # Assuming the maximum size of the heap to be 15.
    h = MaxHeap(15)

    # Asking the user to input the keys:
    k, i, n = 6, 0, 6
    print("Entered 6 keys:- 3, 10, 12, 8, 2, 14 \n")
    h.insertKey(3)
    h.insertKey(10)
    h.insertKey(12)
    h.insertKey(8)
    h.insertKey(2)
    h.insertKey(14)

    # Printing the current size
    # of the heap.
    print("The current size of the heap is "
          + str(h.curSize()) + "\n")
    print("The current heap is ::")
    print(h.arr)
    # Printing the root element which is
    # actually the maximum element.
    print("The current maximum element is " + str(h.getMax())
          + "\n")

    # Printing the size of the heap
    # after deletion.
    print("The current size of the heap is "
          + str(h.curSize()) + "\n")

    # Inserting 2 new keys into the heap.
    h.insertKey(15)
    h.insertKey(5)
    print("The current size of the heap is "
          + str(h.curSize()) + "\n")
    print("The current maximum element is " + str(h.getMax())
          + "\n")
    h.heapSort(h.arr)

    print('After heapsort::', h.arr)