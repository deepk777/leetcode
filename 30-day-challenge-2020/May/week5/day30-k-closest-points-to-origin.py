# K Closest Points to Origin
# We have a list of points on the plane.  Find the K closest points to the origin(0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
#
# You may return the answer in any order.  The answer is guaranteed to be unique(except for the order that it is in.)
#
# Example 1:
# Input: points = [[1, 3], [-2, 2]], K = 1
# Output: [[-2, 2]]
# Explanation:
# The distance between(1, 3) and the origin is sqrt(10).
# The distance between(-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just[[-2, 2]].
#
# Example 2:
# Input: points = [[3, 3], [5, -1], [-2, 4]], K = 2
# Output: [[3, 3], [-2, 4]]
# (The answer[[-2, 4], [3, 3]] would also be accepted.)
#
# Note:
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000

import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []

        # Build a max heap so we have farthest element
        # on top and when we hit limit we can remove it
        # and enter nearest one
        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            if K > 0:
                heapq.heappush(heap, ((-1)*d, (x, y)))
                K -= 1
            else:
                min_distance_elm = heap[0][0]
                if d < abs(min_distance_elm):
                    heapq.heappop(heap)
                    heapq.heappush(heap, ((-1)*d, (x, y)))

        ans = []
        for elm in heap:
            ans.append(elm[1])

        return ans
