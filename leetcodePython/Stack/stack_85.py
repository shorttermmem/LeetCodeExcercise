from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
         # historgram for the current row
        histogram = [0]*len(matrix[0])
        # for each row, update the histogram and calculate the max area
        for row in range(len(matrix)):
            # update the histogram for the current row
            self._updateHistogramForRow(row, matrix, histogram)
            # calculate the max area for the current histogram
            currMaxArea = self._largestHistogramRectangle(histogram)
            maxArea = max(maxArea, currMaxArea)
        return maxArea

    @staticmethod
    def _updateHistogramForRow(row: int, matrix: List[List[str]], histogram: List[int]) -> None:
        # update the histogram for the current row
        for col in range(len(matrix[0])):
            # if the current element is '1', increment the histogram value
            if matrix[row][col] == '1':
                histogram[col] = histogram[col] + 1 # [1, 0, 1, 0, 0]
            else:
                histogram[col] = 0

    @staticmethod
    def _largestHistogramRectangle(heights: List[int]) -> int:
        increaseHeightIndex = [-1]
        maxArea = 0
        heights.append(0)
        # for each height on this row of histogram, calculate the max area
        for i in range(len(heights)):
            newHeight = heights[i]
            # if the current height is smaller than the previous height
            while increaseHeightIndex[-1] != -1:
                maxHeight = heights[increaseHeightIndex[-1]]
                if newHeight > maxHeight:
                    break
                increaseHeightIndex.pop()
                # calculate the area
                smallerHeightIndex = increaseHeightIndex[-1]
                width = i - smallerHeightIndex - 1
                maxArea = max(maxArea, maxHeight*width)
            # add the current height to the stack
            increaseHeightIndex.append(i)
        # remove the last element
        heights.pop()
        return maxArea
