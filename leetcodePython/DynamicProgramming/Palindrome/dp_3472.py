#https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/description/

# Example 1:

# Input: s = "abced", k = 2
# Output: 3

# Explanation:
# Replace s[1] with the next letter, and s becomes "acced".
# Replace s[4] with the previous letter, and s becomes "accec".
# The subsequence "ccc" forms a palindrome of length 3, which is the maximum.

# Example 2:

# Input: s = "aaazzz", k = 4
# Output: 6

# Explanation:
# Replace s[0] with the previous letter, and s becomes "zaazzz".
# Replace s[4] with the next letter, and s becomes "zaazaz".
# Replace s[3] with the next letter, and s becomes "zaaaaz".
# The entire string forms a palindrome of length 6.

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        def cost(c1: str, c2: str) -> int:
            # c1 and c2 are lowercase English letters
            dist = abs(ord(c1) - ord(c2))
            # Returns the cost of changing c1 to c2
            return min(dist, 26 - dist)
        
        n = len(s)
        # dp[i][j][kk] = longest palindromic subsequence in s[i:j+1] with at most kk cost
        dp = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        
        # Base case: single characters
        for i in range(n):
            for kk in range(k + 1):
                dp[i][i][kk] = 1
        
        # iterate over all start indices of s
        for i in range(n - 1, -1, -1):
            # iterate over all end indices of s
            for j in range(i + 1, n):
                # iterate over all costs
                for kk in range(k + 1):
                    if s[i] == s[j]:
                        # we can extend the palindrome
                        # dp[i][j][kk] = dp[i + 1][j - 1][kk] + 2
                        # or if j == i + 1, we have a palindrome of length 2
                        dp[i][j][kk] = 2 if j == i + 1 else dp[i + 1][j - 1][kk] + 2
                    else:
                        # we can't extend the palindrome
                        dp[i][j][kk] = max(dp[i + 1][j][kk], dp[i][j - 1][kk])
                        # Change s[i] or s[j] to match
                        d = cost(s[i], s[j])
                        if d <= kk:
                            # we can change s[i] or s[j] to match
                            dp[i][j][kk] = max(dp[i][j][kk], 
                                              (2 if j == i + 1 else dp[i + 1][j - 1][kk - d] + 2))
        
        return dp[0][n - 1][k]