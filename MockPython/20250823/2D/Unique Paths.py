#https://leetcode.com/problems/unique-paths/description/
from common_types import *

"""
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Two movement option at each location:
* Down y + 1
* Right x + 1

pathsAt[y][x]


Input: m = 3, n = 7
Output: 28
           x, y-1
x-1, y     x, y

(0, 0)(1,0)
(0, 1)(1, 1)

(0, 9)

pathsAt[y][x] = pathsAt[y-1][x] + pathsAt[y][x-1]

uniquePaths(self, x, y) -> int:
    if x == 0 and y == 0:
        return 0
    if x == 0:
        return 1
    if y == 0:
        return 1
    return self.uniquePaths(x-1, y) + self.uniquePaths(x, y-1)
"""
from functools import *

class Solution:
    @cache
    def _uniquePaths(self, x, y) -> int:
        if x == 1 or y == 1:
            return 1
        return self._uniquePaths(x-1, y) + self._uniquePaths(x, y-1)

    def uniquePaths(self, m: int, n: int) -> int:
        return self._uniquePaths(m, n)


class SolutionBottomUp:
    def uniquePaths(self, rows: int, cols: int) -> int:
        # pathsAt[y][x] = pathsAt[y-1][x] + pathsAt[y][x-1]
        pathAt = [[1] * cols for _ in range(rows)]
        for row in range(1, rows):
            for col in range(1, cols):
                pathAt[row][col] = pathAt[row - 1][col] + pathAt[row][col - 1]
        return pathAt[-1][-1]


class SolutionOpt:
    def uniquePaths(self, rows: int, cols: int) -> int:
        # Use the smaller dimension for the array to minimize space
        if rows > cols:
            rows, cols = cols, rows
        
        # Initialize a 1D array for the smaller dimension (rows)
        pathAt = [1] * rows
        
        # Iterate over the larger dimension (cols)
        for _ in range(1, cols):
            # Update each position in the 1D array
            for i in range(1, rows):
                pathAt[i] += pathAt[i - 1]
        
        return pathAt[-1]

from math import factorial

class SolutionMath:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)
    

































    