#https://leetcode.com/problems/palindrome-partitioning-ii/description/
#Return the minimum cuts needed for a palindrome partitioning of s.
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # dp[i] is the minimum cuts needed for a palindrome partitioning of s[:i]
        dp = [0] * n
        # isPalindrome[i][j] is True if s[i:j+1] is a palindrome
        isPalindrome = [[False] * n for _ in range(n)]
        # dp[i] is initialized to i
        # isPalindrome[i][i] is True for all i
        for i in range(n):
            minCut = i
            for j in range(i + 1):
                # s[i] == s[j] and s[j+1:i] is a palindrome
                if s[i] == s[j] and (i - j <= 1 or isPalindrome[j + 1][i - 1]):
                    isPalindrome[j][i] = True
                    # if j == 0, s[:i+1] is a palindrome
                    # so no cut is needed
                    # otherwise, s[j:i+1] is a palindrome
                    # so we can use dp[j - 1] + 1 to update minCut
                    minCut = 0 if j == 0 else min(minCut, dp[j - 1] + 1)
            dp[i] = minCut
        return dp[-1]