#https://leetcode.com/problems/longest-common-subsequence/description/

from common_types import *
"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

# a b c d e 
a 1 1 1 1 1
c 1 1 2
e 1

i1, i2

max(
dp[i1-1]
)

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1[i1] == text2[i2]
        # dp[i1+1] and dp[i2+1] 
        return 0