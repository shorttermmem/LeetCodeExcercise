#https://leetcode.com/problems/palindrome-partitioning-iv/description/
# can split the string s into three non-empty palindromic substrings
# Input: s = "abcbdd"
# Output: true
# Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        # isPalindrome[i][j] is True if s[i:j+1] is a palindrome
        isPalin = [[False] * n for _ in range(n)]
        
        # Try all lengths of palindromes
        for length in range(1, n + 1):
            # Iterate over start index
            for i in range(n - length + 1):
                # End index
                j = i + length - 1
                isPalin[i][j] = (s[i] == s[j]) and (length <= 2 or isPalin[i + 1][j - 1])
        
        # Iterate over all possible split points
        for i in range(1, n - 1):  # First split
            if isPalin[0][i - 1]:  # First part: s[0:i]
                for j in range(i, n - 1):  # Second split
                    if isPalin[i][j] and isPalin[j + 1][n - 1]:  # Second and third parts
                        return True
        return False
    