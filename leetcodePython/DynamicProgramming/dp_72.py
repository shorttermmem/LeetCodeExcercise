#https://leetcode.com/problems/edit-distance/description/?envType=problem-list-v2&envId=dynamic-programming


# Problem: Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.\
# You have the following 3 operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character
# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3


class Solution:

    # top down approach
    def minDistance(self, word1: str, word2: str) -> int:
        
        #  dp[i][j] is the minimum number of operations to convert word1[0..i) to word2[0..j)
        dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]

        def helper(i, j):
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = helper(i - 1, j - 1)
            else:
                dp[i][j] = 1 + min(helper(i, j - 1), helper(i - 1, j), helper(i - 1, j - 1))

            return dp[i][j]

        return helper(len(word1) - 1, len(word2) - 1)
