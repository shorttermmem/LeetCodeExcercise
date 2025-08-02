#https://leetcode.com/problems/as-far-from-land-as-possible/

from common_types import *

"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, 
find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

1 0 1
0 0 0
1 0 1

lvl1
1 1 1
1 0 1
1 1 1



Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 
1 0 0
0 0 0
0 0 0

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100

10^4 data total grid size

grid[i][j] is 0 or 1
"""
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        level = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    level.append((r, c))
        
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def _valid(row, col):
            if row < 0 or row >= len(grid):
                return False
            if col < 0 or col >= len(grid[0]):
                return False
            if grid[row][col] == 1:
                return False
            return True
        
        if not level or len(level) == len(grid) * len(grid[0]):
            return -1
        result = 0
        while level:
            levelSize = len(level)
            for i in range(levelSize):
                land_r, land_c = level.popleft()
                for dir_r, dir_c in directions:
                    new_r, new_c = land_r + dir_r, land_c + dir_c
                    if _valid(new_r, new_c):
                        grid[new_r][new_c] = 1
                        level.append((new_r, new_c))
            result += 1

        return result