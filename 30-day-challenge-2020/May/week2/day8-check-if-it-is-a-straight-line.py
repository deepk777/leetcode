# Check If It Is a Straight Line
# You are given an array coordinates, coordinates[i] = [x, y], where[x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
#
#
# Example 1:
# Input: coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
# Output: true
#
# Example 2:
# Input: coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
# Output: false
#
#
# Constraints:
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10 ^ 4 <= coordinates[i][0], coordinates[i][1] <= 10 ^ 4
# coordinates contains no duplicate point.

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates:
            return False

        if len(coordinates) <= 2:
            return True

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x_slope = (x2-x1)
        if not x_slope:
            slope = 0
        else:
            slope = (y2-y1)/x_slope
        x1, y1 = x2, y2
        for i in range(2, len(coordinates)):
            x2, y2 = coordinates[i]
            x_slope = (x2-x1)
            if not x_slope:
                slope1 = 0
            else:
                slope1 = (y2-y1)/x_slope

            if slope1 != slope:
                return False
            x1, y1 = x2, y2

        return True
