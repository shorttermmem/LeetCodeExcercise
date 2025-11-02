#https://leetcode.com/problems/shortest-path-in-binary-matrix/

from common_types import *

"""
1091. Shortest Path in Binary Matrix
Medium
Topics
premium lock icon
Companies
Hint
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2

left right, top bottom. diagnal
[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

[
[0,1],
[1,0]]

Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

[
[0,0,0],
[1,1,0],
[1,1,0]]

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

[
[1,0,0],
[1,1,0],
[1,1,0]]
[
[1] 
]
Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # handle first one 1 situation later
        if grid[0][0] == 1:
            return -1

        level = deque([(0, 0)])

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        pathCount = 0
        
        def isPosValid(row, col) -> bool:
            if row < 0 or row > len(grid) - 1:
                return False
            if col < 0 or col > len(grid[0]) -1:
                return False
            if grid[row][col] == 1:
                return False
            return True

        while level:
            levelSize = len(level)
            pathCount += 1
            for _ in range(levelSize):
                currRow, currCol = level.popleft()
                if currRow == len(grid) - 1 and currCol == len(grid[0]) - 1:
                    return pathCount
                for dirR, dirC in directions:
                    nextR, nextC = currRow + dirR, currCol + dirC
                    if isPosValid(nextR, nextC):
                        level.append((nextR, nextC))
                        grid[nextR][nextC] = 1 # visited
        return -1