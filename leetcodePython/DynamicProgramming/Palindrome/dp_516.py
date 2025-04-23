#https://leetcode.com/problems/longest-palindromic-subsequence/description/
# Example 1:
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j] represents the longest palindromic subsequence's length between index i and j.
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # Base Case: single character is palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Try all possible subsequence lengths 2 to n
        for length in range(2, n+1):
            # Try all possible starting indices with current length
            for i in range(n - length + 1):
                # ending index of current length substring
                j = i + length - 1
                
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        # extend the palindrome
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # pick the longest from extending the left or the right
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]
