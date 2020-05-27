# Flood Fill
# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image(from 0 to 65535)

# Given a coordinate(sr, sc) representing the starting pixel(row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels(also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

# Example 1:
# Input:
# image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
# Explanation:
# From the center of the image(with position(sr, sc)=(1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.

# Note:
#
# The length of image and image[0] will be in the range[1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].


class Solution(object):

    # def changeColor(self, image, )

    def checkValidPixel(self, image, r, c, color):
        maxR = len(image)
        maxC = len(image[0])
        if r < 0 or r >= maxR or c < 0 or c >= maxC or image[r][c] != color:
            return False
        return True

    def colorFill(self, image, sr, sc, oldColor, newColor):

        image[sr][sc] = newColor

        valid_moves = (
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        )

        for r, c in valid_moves:
            nr, nc = sr + r, sc + c
            if self.checkValidPixel(image, nr, nc, oldColor):
                self.colorFill(image, nr, nc, oldColor, newColor)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        oldColor = image[sr][sc]
        if newColor == oldColor:
            return image
        self.colorFill(image, sr, sc, oldColor, newColor)
        return image
