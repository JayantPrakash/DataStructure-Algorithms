import heapq
import math
from typing import List

import numpy as np


class Solution:
    # Keep k closest points in a max-heap simulated with negative distances.
    # O(n log(k + 1)) time and O(k) space; assumes 1 <= k <= number of points.
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for point in points:
            # Negation makes the farthest retained point the smallest heap key and therefore easiest to evict.
            point_dist = -1 * self.dist_calculate(point)
            if len(heap) < k:
                heapq.heappush(heap, (point_dist, point))
            else:
                # A larger negative key means a smaller real distance, so this point improves the retained set.
                if point_dist > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(point_dist, point))
        output = []
        # Pop retained points from farthest to closest; the returned order is not distance-ascending.
        for i in range(k):
            elem = heapq.heappop(heap)
            output.append(elem[1])
        return output

    # Euclidean distance uses sqrt(x^2+y^2); comparing squared distances would preserve the same ranking.
    def dist_calculate(self,point):
        return math.sqrt(point[0]**2 + point[1]**2)

sol = Solution()
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
points = [[1,3],[-2,2]]
k = 1
points = [[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]]
k = 5
print(sol.kClosest(points, k))
