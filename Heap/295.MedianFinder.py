import heapq as hp
# Maintain a lower half as a max-heap (negated values) and an upper half as a min-heap.
# Every lower value must be <= every upper value, and heap sizes differ by at most one.
class MedianFinder:

    def __init__(self):
        self._small_heap = []
        self._large_heap = []
    # Insert in O(log n), then restore the ordering boundary and the size balance.
    def addNum(self, num: int) -> None:
        hp.heappush(self._small_heap, -1*num)
        # If the lower maximum exceeds the upper minimum, move it across the boundary.
        if self._small_heap and self._large_heap and self._small_heap[0]*-1 > self._large_heap[0]:
            val = hp.heappop(self._small_heap) * -1
            hp.heappush(self._large_heap, val)

        # When one half has two extra values, transfer its boundary value to the other half.
        if len(self._small_heap) - len(self._large_heap) == 2:
            val = hp.heappop(self._small_heap) * -1
            hp.heappush(self._large_heap, val)
        if len(self._large_heap) - len(self._small_heap) == 2:
            val = hp.heappop(self._large_heap)
            hp.heappush(self._small_heap, -1 * val)        


    # Read the middle value(s) in O(1): average both roots for even size, else use the larger half's root.
    # At least one value must have been added; storing the stream takes O(n) space.
    def findMedian(self) -> float:
        if len(self._large_heap) == len(self._small_heap):
            self.median = (self._large_heap[0] + self._small_heap[0] * -1)/2.0    
        elif len(self._large_heap) > len(self._small_heap):
            self.median = self._large_heap[0]
        else:
            self.median = -1 * self._small_heap[0]
        return self.median

# Your MedianFinder object will be instantiated and called as such:
medianFinder = MedianFinder ()
medianFinder.addNum(1);    # arr = [1]
medianFinder.addNum(2);    # arr = [1, 2]
print(medianFinder.findMedian()); # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    # arr[1, 2, 3]
print(medianFinder.findMedian()); # return 2.0