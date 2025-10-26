#https://leetcode.com/problems/minimum-path-sum

from common_types import *

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.


[1,3,1],
[1,5,1],
[4,2,1]

minPathSum[row][col] = min(minPathSum[row-1][col], minPathSum[row][col-1])

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        @cache
        def getMinPathSum(row, col) -> int:
            if row == 0 and col == 0:
                return grid[0][0]

            if row == 0:
                return grid[row][col] + getMinPathSum(row, col-1)

            if col == 0:
                return grid[row][col] + getMinPathSum(row-1, col)

            return grid[row][col] + min(getMinPathSum(row-1, col), getMinPathSum(row, col-1))

        return getMinPathSum(len(grid)-1, len(grid[0])-1)