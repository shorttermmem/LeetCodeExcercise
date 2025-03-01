#https://leetcode.com/problems/triangle/description/
# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

from typing import List

class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        if n == 0:
            return 0
        # Initialize DP array with the last row of the triangle
        dp = triangle[-1].copy()
        # Process each row from the second last up to the top
        for i in range(n-2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]


    def TOO_SLOW_minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # states
        # return curr_sum

        # actions
        # pre-order
        # dfs(left or right)

        # transition
        # min_sum = min(curr_sum, min_sum)
        depth = len(triangle)
        min_sum = float('inf')

        # 1, 2, 3, 4
        # width = depth

        def dfs(node, i, j, curr):
            nonlocal min_sum

            if i < depth:
                curr += node[i][j]

            if i == depth - 1:
                min_sum = min(curr, min_sum)
                #print(min_sum)
                return

            dfs(node, i+1, j, curr)
            if j + 1 < depth:
                dfs(node, i+1, j + 1, curr)

        dfs(triangle, 0, 0, 0)
        return min_sum