#https://leetcode.com/problems/decode-ways/
from common_types import *

"""
Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

230 => C
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        waysToLength = [0] * (len(s) + 1)
        if s[0] != "0":
            waysToLength[1] = 1
        #12
        for digitCount in range(2, len(s)+1):
            index = digitCount - 1
            if s[index] != '0':
                waysToLength[digitCount] = waysToLength[digitCount-1]
            if 10 <= int(s[index-1:index]) < 27:
                waysToLength[digitCount] += waysToLength[digitCount-2]
        return waysToLength[len(s)]