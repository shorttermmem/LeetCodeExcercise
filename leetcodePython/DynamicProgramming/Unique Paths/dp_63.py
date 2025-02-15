#https://leetcode.com/problems/unique-paths-ii/description/
# all roads to Rome with obstacles
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: