#https://leetcode.com/problems/longest-palindromic-substring/description/

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        # dp[i][j] will be 1 if the substring s[i...j] is a palindrome.
        dp = [[0] * n for _ in range(n)]
        
        start, max_length = 0, 1
        
        # Base case: single letter palindromes
        for i in range(n):
            dp[i][i] = 1
        
        # Base case: double letter palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                start = i
                max_length = 2
        
        # The rest of the cases: length 3 to n
        for length in range(3, n + 1):
            # Try all possible starting indices with current length
            # l is the starting index and r is the ending index of substring
            for l in range(n - length + 1):
                r = l + length - 1

                # check if can be extended to l..r from l+1..r-1
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = 1
                    start = l
                    max_length = length
        
        return s[start:start + max_length]