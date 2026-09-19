import heapq
from typing import List


class Solution:
    # Maintain the k largest values in a min-heap; its root is the weakest retained value.
    # O(n log(k + 1)) time and O(k) space; assumes 1 <= k <= len(nums).
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            # Fill the candidate heap before applying any rejection threshold.
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                # Only a value above the current kth largest can improve the retained top k; smaller values are irrelevant.
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        # Duplicates count separately, so this is kth by occurrence rather than kth distinct value.
        return heap[0]

