#https://leetcode.com/problems/longest-common-subsequence/
from common_types import *

"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.



two states
index txt1 and index txt2

longestSubseq[index1][index2]
= longestSubseq for txt1 start index1 and txt2 index2

abcde
ggggbdehhhh

bde

if txt1[ind1] == txt2[ind2]:
    longestSubseq[ind1][ind2] = longestSubseq[ind1-1][ind2-1] + 1
else:
    longestSubseq[ind1][ind2] = max(longestSubseq[ind1-1][ind2], longestSubseq[ind1][ind2-1]

subseq[ind_b+1][]

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        maxLengthSubWith = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for l1 in range(1, len(text1)+1):
            i1 = l1 - 1
            for l2 in range(1, len(text2)+1):
                i2 = l2 - 1
                if text1[i1] == text2[i2]:
                    maxLengthSubWith[l1][l2] = 1 + maxLengthSubWith[l1-1][l2-1]
                else:
                    maxLengthSubWith[l1][l2] = max(maxLengthSubWith[l1-1][l2], maxLengthSubWith[l1][l2-1])
        return maxLengthSubWith[len(text1)][len(text2)]