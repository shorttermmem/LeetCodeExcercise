#https://leetcode.com/problems/palindrome-partitioning-iii/description/
#Return the minimal number of characters that you need to change to divide the string.
# Input: s = "abc", k = 2
# Output: 1
# Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        # Compute cost to make s[i:j+1] a palindrome
        cost = [[0] * n for _ in range(n)]
        # Iterate over palindrome substrings
        for length in range(2, n + 1):
            # Iterate over start index
            for i in range(n - length + 1):
                # End index
                j = i + length - 1
                # Cost to make s[i:j+1] a palindrome
                cost[i][j] = cost[i + 1][j - 1] if length > 2 else 0
                # Update cost if characters are different
                if s[i] != s[j]:
                    cost[i][j] += 1
        
        # dp[i][k] = min changes for s[0:i] with k partitions
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # Empty string with 0 partitions
        
        # Iterate over prefix length
        for i in range(1, n + 1):
            # Iterate over number of partitions
            for p in range(1, min(k + 1, i + 1)):
                # Try last palindrome ending at i-1
                for j in range(p - 1, i):
                    dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j][i - 1])
        
        return dp[n][k]