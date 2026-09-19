# Key idea: Track heap ordering and which element is kept at the root.
import heapq as hp
# Group the state and operations used by the MedianFinder implementation.
class MedianFinder:

    # Initialize the state needed by a new instance.
    def __init__(self):
        self._small_heap = []
        self._large_heap = []
    # Compute or update the add num result for the supplied input.
    def addNum(self, num: int) -> None:
        # add to small heap by default
        hp.heappush(self._small_heap, -1*num)
        # if largest value in small heap is greater than smallest value in large heap, 
        # move the largest value to large heap
        if self._small_heap and self._large_heap and self._small_heap[0]*-1 > self._large_heap[0]:
            val = hp.heappop(self._small_heap) * -1
            hp.heappush(self._large_heap, val)

        # rebalancing    
        if len(self._small_heap) - len(self._large_heap) == 2:
            val = hp.heappop(self._small_heap) * -1
            hp.heappush(self._large_heap, val)
        # Choose this path when `len(self._large_heap) - len(self._small_heap) == 2` is true.
        if len(self._large_heap) - len(self._small_heap) == 2:
            val = hp.heappop(self._large_heap)
            hp.heappush(self._small_heap, -1 * val)        


    # Compute or update the find median result for the supplied input.
    def findMedian(self) -> float:
        # Choose this path when `len(self._large_heap) == len(self._small_heap)` is true.
        if len(self._large_heap) == len(self._small_heap):
            self.median = (self._large_heap[0] + self._small_heap[0] * -1)/2.0    
        # Choose this path when `len(self._large_heap) > len(self._small_heap)` is true.
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