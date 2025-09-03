#https://leetcode.com/problems/longest-palindromic-subsequence/
from common_types import *

"""
Given a string s, find the longest palindromic subsequence's length in s.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".


EBFCGAHCIBJ

BCACB

states:
leftIndex, rightIndex


maxLengthBtw[left][right]

if s[left] == s[right]:
    maxLengthBtw[left][right] = 2 + maxLengthBtw[left+1][right-1]
else:
    maxLengthBtw[left][right] = max(maxLengthBtw[left+1][right], maxLengthBtw[left][right-1])
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        maxLengthBtw = [[0] * len(s) for _ in range(len(s))]
        for right in range(len(s)):
            maxLengthBtw[right][right] = 1
            for left in range(right-1, -1, -1):
                if s[left] == s[right]:
                    maxLengthBtw[left][right] = 2 + maxLengthBtw[left+1][right-1]
                else:
                    maxLengthBtw[left][right] = max(maxLengthBtw[left+1][right], maxLengthBtw[left][right-1])
        return maxLengthBtw[0][len(s)-1]
    
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Initialize DP table
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single characters
        for i in range(n):
            dp[i][i] = 1
        
        # Iterate over substring lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]
    """