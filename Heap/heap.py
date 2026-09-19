# A zero-based complete binary tree stored in an array: each parent dominates both children.
# heapSize counts live values; maxSize is allocated capacity, including unused slots.
class MaxHeap:
    arr = []
    maxSize = 0
    heapSize = 0

    def __init__(self, maxsize):
        self.maxSize = maxsize
        self.heapSize = 0
        self.arr = [None] * maxsize

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return int((i - 1) / 2)

    # Repair one downward violation assuming both child subtrees already satisfy max-heap order.
    def MaxHeapify(self, i):
        l = self.left(i)
        r = self.right(i)

        largest = i

        if self.heapSize == 0 or self.heapSize == 1:
            return

        if l < self.heapSize and self.arr[l] > self.arr[largest]:
            largest = l

        if r < self.heapSize and self.arr[r] > self.arr[largest]:
            largest = r

        # Swap with the larger child, then repair only the subtree receiving the displaced value.
        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.MaxHeapify(largest)

    # Replace the root with the last live element and sift down in O(log n).
    # This version returns root only for a singleton; the multi-element branch currently returns None.
    def removeMax(self):
        if self.heapSize == 0:
            return None
        root = self.arr[0]
        if self.heapSize == 1:
            self.arr[0] = None
            self.heapSize -= 1
            return root

        self.arr[0] = self.arr[self.heapSize - 1]
        self.heapSize -= 1
        self.MaxHeapify(0)

    # Append at the next leaf and bubble upward while a parent is smaller: O(log n).
    def insertKey(self, x):
        if self.heapSize == self.maxSize:
            return 'Max elem reached'

        self.heapSize += 1
        i = self.heapSize - 1
        self.arr[i] = x

        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = self.arr[i]
            self.arr[i] = temp
            i = self.parent(i)

    def curSize(self):
        return self.heapSize

    # The heap invariant puts the maximum at index 0, giving O(1) access.
    def getMax(self):
        return self.arr[0]

    # Intended heapsort needs a shrinking active heap and a root repair after each swap.
    # This version keeps heapSize unchanged and heapifies i instead of 0, so it is not a correct general heapsort.
    def heapSort(self,arr):
        N = self.heapSize

        # Build a maxheap.
        # Bottom-up construction works because leaves already satisfy the heap property.
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

    # The example inserts fixed values below; it does not read interactive input.
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