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
        
        # states
        # ways_to_curr[i][j]

        # actions
        # ways_to_curr[i][j] = ways_to_curr[i-1][j] + ways_to_curr[i][j-1]

        # transitions
        # ways_to_curr[i][j] = 0 if obstacleGrid[i][j] else (ways_to_curr[i-1][j] + ways_to_curr[i][j-1])
        def tabulation():
            h, w = len(obstacleGrid), len(obstacleGrid[0])
            ways_to_curr = [[0] * (w+1)] * (h + 1)

            ways_to_curr[1][1] = 1
            for i in range(1, h+1):
                for j in range(1, w+1):
                    ways_to_curr[i][j] = 0 if obstacleGrid[i - 1][j - 1] == 1 else (ways_to_curr[i-1][j] + ways_to_curr[i][j-1])
            
            return ways_to_curr[-1][-1]

        # referencing max 1, requires only two variables, left and top
        def tabulation_with_memory_opt():
            h, w = len(obstacleGrid) + 1, len(obstacleGrid[0]) + 1

            #       | top[0 .. w]
            #  left | ways_to_curr
            ways_to_curr = 1
            left = 0
            top = [0] * (w)
            
            top[1] = 1
            for i in range(1, h):
                for j in range(1, w):
                    if j == 1:
                        left = 0

                    if obstacleGrid[i - 1][j - 1] == 1:
                        left, top[j] = 0, 0
                              
                    ways_to_curr = left + top[j]                    
                    left = ways_to_curr
                    top[j] = ways_to_curr    

            return ways_to_curr