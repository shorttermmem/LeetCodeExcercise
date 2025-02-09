#https://leetcode.com/problems/unique-paths/description/
from itertools import product

class Solution:
    # bottom-up approach with tabulation
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = number of unique paths to reach (i, j)
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # base case: dp[0][j] = 1, dp[i][0] = 1
        dp = [[1] * n for _ in range(m)]
        
        for i,j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        return dp[-1][-1]                
        
    # top-down approach with memoization
    def uniquePaths2(self, m: int, n: int) -> int:
        
        def _recur(m, n, memo):
            if m == 1 or n == 1:
                return 1
            
            if (m, n) in memo:
                return memo[(m, n)]
            
            memo[(m, n)] = _recur(m-1, n, memo) + _recur(m, n-1, memo)
            return memo[(m, n)]
        return _recur(m, n, {})
    
    # brute force
    def uniquePaths3(self, m: int, n: int) -> int:
        def _recur(m, n):
            if m == 1 or n == 1:
                return 1
            return _recur(m-1, n) + _recur(m, n-1)
        return _recur(m, n)